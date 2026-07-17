"use strict";

/* ==========================================================================
   VIDHWAAN AI Writer
   Prompt Builder
   ========================================================================== */

const VWPrompt = (() => {

    function clean(value) {

        return String(value || "")
            .trim();

    }

    function build(data = {}) {

        const lines = [

            "You are VIDHWAAN AI Writer.",

            "Create high quality professional content.",

            "",

            `Purpose: ${clean(data.purpose)}`,

            `Category: ${clean(data.category)}`,

            `Writing Style: ${clean(data.style)}`,

            `Target Audience: ${clean(data.audience)}`,

            `Content Length: ${clean(data.length)}`,

            `Platform: ${clean(data.platform)}`,

            `Language: ${clean(data.language)}`,

            `Creativity: ${clean(data.creativity)}`,

            `Emoji Usage: ${clean(data.emoji)}`,

            `Call To Action: ${clean(data.cta)}`,

            "",

            "Topic:",

            clean(data.topic),

            "",

            "Additional Instructions:",

            clean(data.instructions)

        ];

        return lines
            .join("\n")
            .trim();

    }

    return Object.freeze({

        build

    });

})();
