"use strict";

/* ==========================================================================
   VIDHWAAN AI Writer
   Prompt Builder

   Converts user selections into AI prompt

   ========================================================================== */


const PromptBuilder = {



    build(context = {}) {


        const lines = [


            "Create high quality content using the following requirements.",


            "",


            `Purpose: ${context.purpose || ""}`,

            `Category: ${context.category || ""}`,

            `Topic: ${context.topic || ""}`,

            `Goal: ${context.goal || ""}`,

            `Content Style: ${context.contentStyle || ""}`,

            `Audience: ${context.audience || ""}`,

            `Length: ${context.length || ""}`,



            "",


            "Advanced Preferences:",


            `Platform: ${context.platform || ""}`,

            `Language: ${context.language || ""}`,

            `Creativity: ${context.creativity || ""}`,

            `Emoji Usage: ${context.emoji || ""}`,

            `Call To Action: ${context.cta || ""}`,



            "",


            "Write clear, useful, accurate, and engaging content."

        ];





        return lines.join("\n").trim();


    }


};





export default PromptBuilder;