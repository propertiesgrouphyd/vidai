"use strict";

/* ==========================================================================
   VIDHWAAN AI Writer
   AI Client

   Handles only Groq API communication

   ========================================================================== */


const AIClient = {



    async generate(

        prompt,

        apiKey

    ){



        if(!prompt){

            throw new Error(
                "Prompt is required."
            );

        }



        if(!apiKey){

            throw new Error(
                "API key not configured."
            );

        }






        const response =

        await fetch(

            VW_CONFIG.API.BASE_URL +

            VW_CONFIG.API.CHAT_ENDPOINT,


            {


                method:"POST",


                headers:{


                    "Content-Type":
                    "application/json",



                    "Authorization":
                    `Bearer ${apiKey}`


                },



                body:JSON.stringify({


                    model:

                    VW_CONFIG.API.MODEL,



                    messages:[


                        {


                            role:"user",


                            content:prompt


                        }


                    ],




                    temperature:0.7,



                    max_tokens:4096


                })


            }


        );







        if(!response.ok){


            const error =
            await response.text();


            throw new Error(

                "AI request failed: "

                +

                error

            );


        }








        const data =

        await response.json();







        return (

            data

            ?.choices

            ?. [0]

            ?.message

            ?.content

            ||

            ""

        );


    }



};





export default AIClient;