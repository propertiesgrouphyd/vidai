"use strict";

import DataManager from "./data-manager.js";



function populateSelect(
    select,
    items = [],
    placeholder = "Select"
){

    if(!select){
        return;
    }



    select.innerHTML = "";



    const first = document.createElement("option");

    first.value = "";

    first.textContent = placeholder;

    first.disabled = true;

    first.selected = true;

    select.appendChild(first);





    if(!items || items.length === 0){

        return;

    }





    const uniqueItems =

    items.filter(

        (item,index,self)=>

            item.id &&

            index === self.findIndex(

                x => x.id === item.id

            )

    );





    uniqueItems.forEach(item=>{


        const option =
        document.createElement("option");



        option.value =
        item.id;



        option.textContent =
        item.label;



        select.appendChild(option);


    });


}







const DropdownManager = Object.freeze({



    /*
        Purpose
    */

    populatePurposes(select){

        populateSelect(

            select,

            DataManager.getPurposes(),

            "Select Purpose"

        );

    },






    /*
        Category
    */


    clearCategories(select){

        populateSelect(

            select,

            [],

            "Select Category"

        );

    },




    populateCategoriesByPurpose(
        select,
        purpose
    ){

        populateSelect(

            select,

            DataManager.getCategoriesByPurpose(
                purpose
            ),

            "Select Category"

        );

    },







    /*
        Topics
    */


    clearTopics(select){

        populateSelect(

            select,

            [],

            "Select Topic"

        );

    },





    populateTopicsByCategory(
        select,
        category
    ){

        populateSelect(

            select,

            DataManager.getTopicsByCategory(
                category
            ),

            "Select Topic"

        );

    },






    /*
        Load all categories/topics
        (optional)
    */


    populateCategories(select){

        populateSelect(

            select,

            DataManager.getCategories(),

            "Select Category"

        );

    },





    populateTopics(select){


        const topics = [

            ...DataManager.getTopics(),

            {
                id:"custom-topic",
                label:"Custom Topic"
            }

        ];



        populateSelect(

            select,

            topics,

            "Select Topic"

        );


    },







    /*
        Independent dropdowns
    */


    populateGoals(select){

        populateSelect(

            select,

            DataManager.getGoals(),

            "Select Goal"

        );

    },




    populateContentStyles(select){

        populateSelect(

            select,

            DataManager.getContentStyles(),

            "Select Content Style"

        );

    },




    populateAudiences(select){

        populateSelect(

            select,

            DataManager.getAudiences(),

            "Select Audience"

        );

    },




    populateLengths(select){

        populateSelect(

            select,

            DataManager.getLengths(),

            "Select Length"

        );

    },




    populatePlatforms(select){

        populateSelect(

            select,

            DataManager.getPlatforms(),

            "Select Platform"

        );

    },




    populateLanguages(select){

        populateSelect(

            select,

            DataManager.getLanguages(),

            "Select Language"

        );

    },




    populateCreativity(select){

        populateSelect(

            select,

            DataManager.getCreativityLevels(),

            "Select Creativity"

        );

    },




    populateEmojis(select){

        populateSelect(

            select,

            DataManager.getEmojiOptions(),

            "Select Emoji Style"

        );

    },




    populateCTAs(select){

        populateSelect(

            select,

            DataManager.getCTAOptions(),

            "Select Call To Action"

        );

    }



});



export default DropdownManager;