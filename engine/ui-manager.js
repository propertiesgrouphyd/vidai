import DropdownManager from "./dropdown-manager.js";

const UI = {

    purpose: document.getElementById("vw-purpose"),
    category: document.getElementById("vw-category"),
    topic: document.getElementById("vw-topic"),

    customTopic:
        document.getElementById("vw-custom-topic"),
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

    DropdownManager.clearCategories(
        UI.category
    );

    DropdownManager.clearTopics(
        UI.topic
    );

    DropdownManager.populateGoals(UI.goal);

    DropdownManager.populateContentStyles(UI.contentStyle);

    DropdownManager.populateAudiences(UI.audience);

    DropdownManager.populateLengths(UI.length);

    DropdownManager.populatePlatforms(UI.platform);

    DropdownManager.populateLanguages(UI.language);

    DropdownManager.populateCreativity(UI.creativity);

    DropdownManager.populateEmojis(UI.emoji);

    DropdownManager.populateCTAs(UI.cta);

    initializeCascadeDropdowns();

}




function initializeCascadeDropdowns() {

    if (UI.purpose) {

        UI.purpose.addEventListener(
            "change",
            () => {

                DropdownManager.populateCategoriesByPurpose(
                    UI.category,
                    UI.purpose.value
                );

                DropdownManager.populateTopicsByCategory(
                    UI.topic,
                    ""
                );

            }
        );

    }



    if (UI.topic) {

        UI.topic.addEventListener(
            "change",
            () => {

                const wrapper =
                    document.getElementById(
                        "vw-custom-topic-wrapper"
                    );

                if (!wrapper) return;


                if (UI.topic.value === "custom-topic") {

                    wrapper.hidden = false;

                } else {

                    wrapper.hidden = true;

                    if (UI.customTopic) {

                        UI.customTopic.value = "";

                    }

                }

            }
        );

    }


    if (UI.category) {

        UI.category.addEventListener(
            "change",
            () => {

                DropdownManager.populateTopicsByCategory(
                    UI.topic,
                    UI.category.value
                );

            }
        );

    }

}


function getValues() {

    return {

        purpose: UI.purpose?.value || "",

        category: UI.category?.value || "",

        topic:
            UI.topic?.value === "custom-topic"
                ? UI.customTopic?.value || ""
                : UI.topic?.value || "",

        customTopic:
            UI.customTopic?.value || "",

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
