"use strict";


const fs = require("fs");
const path = require("path");



const ROOT =
    path.join(__dirname, "..");



const CATEGORY_FILE =
    path.join(ROOT, "categories.js");


const OUTPUT_FILE =
    path.join(ROOT, "generated", "topics.js");


const PROGRESS_FILE =
    path.join(ROOT, "generated", "topics-progress.json");



const GROQ_API_KEY =
    process.env.GROQ_API_KEY;



const MODEL =
    "llama-3.3-70b-versatile";





function sleep(ms){

    return new Promise(
        resolve => setTimeout(resolve, ms)
    );

}





function loadArrayFromJS(filePath, variableName){


    const content =
        fs.readFileSync(
            filePath,
            "utf8"
        );



    const start =
        content.indexOf(
            `const ${variableName}`
        );



    if(start === -1){

        throw new Error(
            `${variableName} not found`
        );

    }



    const arrayStart =
        content.indexOf(
            "[",
            start
        );



    let depth = 0;

    let end = -1;



    for(
        let i=arrayStart;
        i<content.length;
        i++
    ){


        if(content[i]==="[")
            depth++;



        if(content[i]==="]"){

            depth--;


            if(depth===0){

                end=i;

                break;

            }

        }


    }



    return eval(
        content.substring(
            arrayStart,
            end+1
        )
    );


}






function getCategories(){


    return loadArrayFromJS(
        CATEGORY_FILE,
        "VW_CATEGORIES"
    );


}







function cleanJSON(text){


    text =
        text
        .replace(/```json/g,"")
        .replace(/```/g,"")
        .trim();



    const start =
        text.indexOf("[");



    const end =
        text.lastIndexOf("]");



    if(start!==-1 && end!==-1){

        text =
            text.substring(
                start,
                end+1
            );

    }



    return text;


}






async function callGroq(prompt){



    let delay =
        60000;



    while(true){



        const response =
            await fetch(
            "https://api.groq.com/openai/v1/chat/completions",
            {


            method:"POST",


            headers:{


                "Authorization":
                `Bearer ${GROQ_API_KEY}`,


                "Content-Type":
                "application/json"


            },


            body:JSON.stringify({


                model:MODEL,


                temperature:0.2,


                messages:[

                    {

                    role:"user",

                    content:prompt

                    }

                ]


            })


            });



        const data =
            await response.json();





        if(response.ok && data.choices){



            return JSON.parse(
                cleanJSON(
                    data.choices[0]
                    .message
                    .content
                )
            );


        }






        if(response.status===429){



            const retry =
                response.headers.get(
                    "retry-after"
                );



            const wait =
                retry
                ?
                Number(retry)*1000
                :
                delay;



            console.log(
                `Groq limit. Waiting ${Math.round(wait/1000)} seconds`
            );



            await sleep(wait);



            delay =
                Math.min(
                    delay*2,
                    900000
                );



            continue;


        }





        console.log(data);



        throw new Error(
            "Groq API failed"
        );


    }


}

// ============================================================
// TOPIC GENERATION ENGINE
// ============================================================



async function generateCategoryTopics(categories){


const prompt = `

You are a world-class LinkedIn content strategist.


Generate professional LinkedIn topic ideas.


Categories:


${categories.map(c=>`

Category ID:
${c.id}

Category Name:
${c.label}

Category Description:
${c.description}

`).join("\n")}



Rules:

Generate exactly 20 topics for EACH category.

Topics must be:

- Professional
- Global audience
- Evergreen
- Useful
- Actionable

Avoid:

- Hashtags
- Emojis
- Duplicate ideas
- Generic words



Return ONLY JSON.


Format:


[
{
"id":"short-kebab-case-id",
"label":"Topic Name",
"category":"category-id",
"description":"Short explanation"
}
]


`;



return await callGroq(prompt);



}








function removeDuplicates(topics){



const seen =
new Set();



return topics.filter(t=>{


const key =
t.id.toLowerCase();



if(seen.has(key)){

return false;

}



seen.add(key);


return true;



});


}








function validateTopic(topic){



return (

topic &&
typeof topic.id==="string" &&
typeof topic.label==="string" &&
typeof topic.category==="string" &&
typeof topic.description==="string"

);

}








function getCategoryTopics(topics,id){


return topics.filter(
t=>t.category===id
);


}








async function repairCategory(category,existing){



const missing =
20-existing.length;



if(missing<=0){

return existing;

}





console.log(
`Repairing ${category.label}: Need ${missing}`
);




const prompt = `


Generate ${missing} additional LinkedIn topics.


Category:

${category.label}


Description:

${category.description}



Existing topics:

${existing.map(t=>t.label).join(", ")}



Do not repeat existing topics.


Return ONLY JSON.


Format:


[
{
"id":"short-kebab-case-id",
"label":"Topic Name",
"category":"${category.id}",
"description":"Short explanation"
}
]


`;



const extra =
await callGroq(prompt);



return [

...existing,

...extra

];


}








async function ensureCategoryComplete(category,topics){



let current =
getCategoryTopics(
topics,
category.id
);



current =
current.filter(
validateTopic
);



current =
removeDuplicates(
current
);





while(current.length < 20){


current =
await repairCategory(
category,
current
);



current =
removeDuplicates(
current
);



}




if(current.length > 20){


current =
current.slice(
0,
20
);


}




return current;


}








function saveProgress(topics){



fs.mkdirSync(

path.dirname(PROGRESS_FILE),

{
recursive:true
}

);



fs.writeFileSync(

PROGRESS_FILE,

JSON.stringify(
topics,
null,
4
)

);


}








function loadProgress(){



if(
!fs.existsSync(PROGRESS_FILE)
){

return [];

}



return JSON.parse(

fs.readFileSync(
PROGRESS_FILE,
"utf8"
)

);



}

// ============================================================
// FINAL GENERATION FLOW
// ============================================================



function createTopicsFile(topics){



const output =

`"use strict";

/* ==========================================================================
   VIDHWAAN AI Writer

   Generated Topic Library

   Auto Generated By GitHub Actions + Groq AI

   Flow:

   Purpose → Category → Topic
   ========================================================================== */


const VW_TOPICS = Object.freeze(

${JSON.stringify(topics,null,4)}

);


Object.freeze(VW_TOPICS);


export default VW_TOPICS;
`;




fs.mkdirSync(

path.dirname(OUTPUT_FILE),

{
recursive:true
}

);



fs.writeFileSync(

OUTPUT_FILE,

output

);



}










function validateFinalTopics(topics){



console.log(
"Validating topics..."
);



const ids =
new Set();



for(const topic of topics){



if(!validateTopic(topic)){


throw new Error(
"Invalid topic found"
);


}





if(ids.has(topic.id)){


throw new Error(
"Duplicate id: "+topic.id
);


}



ids.add(topic.id);



}




console.log(
"Validation successful"
);



console.log(
"Total topics:",
topics.length
);



}









async function generateTopics(){



if(!GROQ_API_KEY){


throw new Error(
"GROQ_API_KEY missing"
);


}





const categories =
getCategories();



console.log(
"Categories:",
categories.length
);





let topics =
loadProgress();



console.log(
"Existing topics:",
topics.length
);





for(
let i=0;
i<categories.length;
i++
){



const category =
categories[i];



let existing =
getCategoryTopics(
topics,
category.id
);





if(existing.length===20){


console.log(
"Skipping:",
category.label
);


continue;


}





console.log(

`Generating:
${category.label}`

);







if(existing.length===0){



const generated =
await generateCategoryTopics(
[category]
);



topics.push(
...generated
);



}







let completed =
await ensureCategoryComplete(
category,
topics
);






topics =
topics.filter(
t=>t.category!==category.id
);



topics.push(
...completed
);





saveProgress(
topics
);





console.log(

`${category.label}:`,
completed.length,
"topics saved"

);





// small delay between categories

await sleep(10000);



}





validateFinalTopics(
topics
);



createTopicsFile(
topics
);





console.log(
"================================"
);



console.log(
"COMPLETED"
);



console.log(
"Topics:",
topics.length
);



console.log(
"================================"
);



}










function validateCommand(){



if(
!fs.existsSync(PROGRESS_FILE)
){


throw new Error(
"No progress file found"
);


}



const topics =
loadProgress();



validateFinalTopics(
topics
);



}











// ============================================================
// START
// ============================================================


if(
process.argv.includes("--validate")
){


validateCommand();


}
else{


generateTopics()
.catch(err=>{


console.error(err);


process.exit(1);


});


}
