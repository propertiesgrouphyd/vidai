"use strict";


function getOutputElement() {

    return document.getElementById(
        "vw-output"
    );

}


function render(content = "") {

    const output = getOutputElement();

    if (!output) return;

    output.textContent = content;

}


function clear() {

    const output = getOutputElement();

    if (!output) return;

    output.textContent = "";

}


async function copy() {

    const output = getOutputElement();

    if (!output) return false;


    const text = output.textContent.trim();


    if (!text) return false;


    await navigator.clipboard.writeText(text);


    return true;

}


export {

    render,

    clear,

    copy

};
