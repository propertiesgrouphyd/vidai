from pathlib import Path

content = '''\
"use strict";

import { initializeDropdowns, getValues } from "./ui-manager.js";
import { validate } from "./validator.js";
import { save } from "./storage.js";
import { buildContext } from "./context-builder.js";
import { buildPrompt } from "./prompt-builder.js";
import { generateContent } from "./ai-client.js";
import * as Output from "./output-renderer.js";

async function onGenerate() {

    const values = getValues();

    const result = validate(values);

    if (!result.valid) {
        alert(result.message);
        return;
    }

    save(values);

    const context = buildContext(values);

    const prompt = buildPrompt(context);

    try {

        const content = await generateContent(prompt);

        Output.render(content);

    } catch (error) {

        console.error(error);

        Output.render("Unable to generate content.");

    }

}

document.addEventListener("DOMContentLoaded", () => {

    initializeDropdowns();

    const button = document.getElementById("vw-generate-btn");

    if (button) {

        button.addEventListener("click", onGenerate);

    }

});
'''

Path("engine/app.js").write_text(content, encoding="utf-8")

print("Updated engine/app.js")
