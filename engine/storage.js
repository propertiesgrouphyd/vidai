"use strict";


const STORAGE_KEY = "vidhwaan-ai-preferences";


function save(values = {}) {

    const data = {

        purpose: values.purpose || "",

        category: values.category || "",

        topic: values.topic || "",

        goal: values.goal || "",

        contentStyle: values.contentStyle || "",

        audience: values.audience || "",

        length: values.length || "",

        platform: values.platform || "",

        language: values.language || "",

        creativity: values.creativity || "",

        emoji: values.emoji || "",

        cta: values.cta || ""

    };


    localStorage.setItem(

        STORAGE_KEY,

        JSON.stringify(data)

    );


    return data;

}


function load() {

    const value =
        localStorage.getItem(STORAGE_KEY);


    if (!value) {

        return {};

    }


    try {

        return JSON.parse(value);

    }

    catch {

        return {};

    }

}


function clear() {

    localStorage.removeItem(STORAGE_KEY);

}


export {

    save,

    load,

    clear

};
