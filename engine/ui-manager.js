import DropdownManager from "./dropdown-manager.js";

const UI = {

    purpose: document.getElementById("vw-purpose"),
    category: document.getElementById("vw-category"),
    topic: document.getElementById("vw-topic"),
    goal: document.getElementById("vw-goal"),

    contentStyle: document.getElementById("vw-style"),
    audience: document.getElementById("vw-audience"),
    length: document.getElementById("vw-length"),

    platform: document.getElementById("vw-platform"),
    language: document.getElementById("vw-language"),
    creativity: document.getElementById("vw-creativity"),

    emoji: document.getElementById("vw-emoji"),
    cta: document.getElementById("vw-cta")

};


function initializeDropdowns() {

    DropdownManager.populatePurposes(UI.purpose);

    DropdownManager.populateCategories(UI.category);

    DropdownManager.populateTopics(UI.topic);

    DropdownManager.populateGoals(UI.goal);

    DropdownManager.populateContentStyles(UI.contentStyle);

    DropdownManager.populateAudiences(UI.audience);

    DropdownManager.populateLengths(UI.length);

    DropdownManager.populatePlatforms(UI.platform);

    DropdownManager.populateLanguages(UI.language);

    DropdownManager.populateCreativity(UI.creativity);

    DropdownManager.populateEmojis(UI.emoji);

    DropdownManager.populateCTAs(UI.cta);

}


function getValues() {

    return {

        purpose: UI.purpose?.value || "",

        category: UI.category?.value || "",

        topic: UI.topic?.value || "",

        goal: UI.goal?.value || "",

        contentStyle: UI.contentStyle?.value || "",

        audience: UI.audience?.value || "",

        length: UI.length?.value || "",

        platform: UI.platform?.value || "",

        language: UI.language?.value || "",

        creativity: UI.creativity?.value || "",

        emoji: UI.emoji?.value || "",

        cta: UI.cta?.value || ""

    };

}


export {

    UI,

    initializeDropdowns,

    getValues

};
