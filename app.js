"use strict";

/* ========================================================================
   VIDHWAAN AI Writer
   Application Bootstrap
   ======================================================================== */

const VWApp = (() => {

    const DOM = {};

    function cacheDOM() {

        DOM.form = document.getElementById("vw-generator-form");

        DOM.output = document.getElementById("vw-output");

        DOM.empty = document.getElementById("vw-empty-state");

        DOM.generate = document.getElementById("vw-generate-btn");

        DOM.apiKey = document.getElementById("vw-api-key");

        DOM.topic = document.getElementById("vw-topic");

        DOM.instructions = document.getElementById("vw-instructions");

    }

    function initialize() {

        cacheDOM();

        VWDropdown.initialize();

        console.log(
            `${VW_CONFIG.APP_NAME} v${VW_CONFIG.APP_VERSION} initialized.`
        );

    }

    return Object.freeze({

        initialize,

        DOM

    });

})();

document.addEventListener("DOMContentLoaded", () => {

    VWApp.initialize();

});

(function () {

    function restoreSettings() {

        const apiKey = VWStorage.getString(
            VW_CONFIG.STORAGE_KEYS.API_KEY,
            ""
        );

        if (VWApp.DOM.apiKey && apiKey) {

            VWApp.DOM.apiKey.value = apiKey;

        }

    }

    async function generateContent(event) {

        event.preventDefault();

        try {

            VWUI.showLoading();

            const apiKey = VWApp.DOM.apiKey.value.trim();

            if (apiKey) {

                VWStorage.setString(
                    VW_CONFIG.STORAGE_KEYS.API_KEY,
                    apiKey
                );

            }

            const prompt = VWPrompt.build({

                purpose: document.getElementById("vw-purpose")?.value,

                category: document.getElementById("vw-category")?.value,

                style: document.getElementById("vw-style")?.value,

                audience: document.getElementById("vw-audience")?.value,

                length: document.getElementById("vw-length")?.value,

                platform: document.getElementById("vw-platform")?.value,

                language: document.getElementById("vw-language")?.value,

                creativity: document.getElementById("vw-creativity")?.value,

                emoji: document.getElementById("vw-emoji")?.value,

                cta: document.getElementById("vw-cta")?.value,

                topic: VWApp.DOM.topic.value,

                instructions: VWApp.DOM.instructions.value

            });

            const output = await VWAI.generate(prompt);

            VWUI.setText("#vw-output", output);

            VWUI.hide("#vw-empty-state");

            VWUI.show("#vw-output");

            VWUI.showToast("Content generated successfully.");

        } catch (error) {

            console.error(error);

            VWUI.showToast(error.message || "Generation failed.");

        } finally {

            VWUI.hideLoading();

        }

    }

    document.addEventListener("DOMContentLoaded", () => {

        restoreSettings();

        if (VWApp.DOM.form) {

            VWApp.DOM.form.addEventListener(
                "submit",
                generateContent
            );

        }

    });

})();