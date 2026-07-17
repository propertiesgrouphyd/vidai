"use strict";


async function generateContent(prompt, config = {}) {

    if (!prompt) {

        throw new Error("Prompt is required.");

    }


    if (!config.apiKey) {

        throw new Error("API key not configured.");

    }


    const response = await fetch(

        config.baseUrl,

        {

            method: "POST",

            headers: {

                "Content-Type": "application/json",

                "Authorization":
                    `Bearer ${config.apiKey}`

            },

            body: JSON.stringify({

                model: config.model,

                messages: [

                    {

                        role: "user",

                        content: prompt

                    }

                ],

                temperature:
                    config.temperature ?? 0.7,

                max_tokens:
                    config.maxTokens ?? 4096

            })

        }

    );


    if (!response.ok) {

        throw new Error(
            "AI request failed."
        );

    }


    const data = await response.json();


    return (

        data?.choices?.[0]?.message?.content
        || ""

    );

}


export {

    generateContent

};
