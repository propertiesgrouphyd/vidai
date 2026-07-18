"use strict";

/* ==========================================================================
   VIDHWAAN AI Writer
   Application Controller
   ========================================================================== */


import {
    UI,
    initializeDropdowns,
    getValues
} from "./ui-manager.js";


import Storage from "./storage.js";

import PaymentManager from "./payment-manager.js";

import SubscriptionManager from "./subscription-manager.js";

import AIClient from "./ai-client.js";

import PromptBuilder from "./prompt-builder.js";





const App = {



    init(){


        initializeDropdowns();


        this.bindEvents();


        this.restoreApiKey();


        console.log(
            "VIDHWAAN AI Writer Ready"
        );


    },





    bindEvents(){


        const form =
        document.getElementById(
            "vw-generator-form"
        );



        if(form){

            form.addEventListener(
                "submit",
                this.generate.bind(this)
            );

        }



        const subscriptionButton =
        document.getElementById(
            "vw-subscription-btn"
        );



        if(subscriptionButton){

            subscriptionButton.addEventListener(

                "click",

                this.subscribe.bind(this)

            );

        }



        const apiButton =
        document.getElementById(
            "vw-api-link-btn"
        );



        if(apiButton){

            apiButton.addEventListener(

                "click",

                ()=>{

                    window.open(

                        "https://console.groq.com/keys",

                        "_blank"

                    );

                }

            );

        }



        const saveApiButton =
        document.getElementById(
            "vw-save-api-btn"
        );



        if(saveApiButton){

            saveApiButton.addEventListener(

                "click",

                ()=>{

                    const input =
                    document.getElementById(
                        "vw-api-key"
                    );


                    Storage.saveApiKey(
                        input.value.trim()
                    );


                    this.closeApiModal();


                }

            );

        }



    },





    restoreApiKey(){


        const key =
        Storage.getApiKey();



        const input =
        document.getElementById(
            "vw-api-key"
        );



        if(
            input &&
            key
        ){

            input.value = key;

        }


    },







    async subscribe(){


        try{


            const result =
            await PaymentManager.start();


            Storage.saveSubscription(
                result
            );



            alert(
                "Subscription activated"
            );


        }
        catch(error){


            alert(
                error.message
            );


        }


    },








    async generate(event){


        event.preventDefault();



        try{



            const apiKey =
            Storage.getApiKey();



            if(!apiKey){


                this.openApiModal();


                return;


            }






            const subscription =

            await SubscriptionManager.check();






            if(!subscription.active){


                document
                .getElementById(
                    "vw-payment-modal"
                )
                .hidden = false;


                return;


            }







            const values =
            getValues();





            const prompt =
            PromptBuilder.build(
                values
            );





            const output =
            await AIClient.generate(
                prompt,
                apiKey
            );





            const result =
            document.getElementById(
                "vw-output"
            );


            result.innerText =
            output;



        }
        catch(error){


            console.error(error);


            alert(
                error.message
            );


        }



    },







    openApiModal(){


        const modal =
        document.getElementById(
            "vw-api-modal"
        );


        if(modal){

            modal.hidden=false;

        }


    },





    closeApiModal(){


        const modal =
        document.getElementById(
            "vw-api-modal"
        );


        if(modal){

            modal.hidden=true;

        }


    }


};






document.addEventListener(

"DOMContentLoaded",

()=>{

    App.init();

}

);