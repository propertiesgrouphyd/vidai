from pathlib import Path

file = Path("engine/app.js")
text = file.read_text(encoding="utf-8")

# Add import only if missing
if "import * as Output" not in text:
    text = text.replace(
        'import { generateContent } from "./ai-client.js";',
        'import { generateContent } from "./ai-client.js";\nimport * as Output from "./output-renderer.js";'
    )

# Add handlers
handlers = '''

async function onCopy() {

    await Output.copy();

}

function onClear() {

    Output.clear();

}

async function onRegenerate() {

    await onGenerate();

}

'''

if "function onClear()" not in text:
    text = text.replace(
        'document.addEventListener("DOMContentLoaded", () => {',
        handlers + '\ndocument.addEventListener("DOMContentLoaded", () => {'
    )

old = '''
    const button = document.getElementById("vw-generate-btn");

    if (button) {

        button.addEventListener("click", onGenerate);

    }
'''

new = '''
    const button = document.getElementById("vw-generate-btn");
    const copyButton = document.getElementById("vw-copy-btn");
    const regenerateButton = document.getElementById("vw-regenerate-btn");
    const clearButton = document.getElementById("vw-clear-btn");

    if (button) {
        button.addEventListener("click", onGenerate);
    }

    if (copyButton) {
        copyButton.addEventListener("click", onCopy);
    }

    if (regenerateButton) {
        regenerateButton.addEventListener("click", onRegenerate);
    }

    if (clearButton) {
        clearButton.addEventListener("click", onClear);
    }
'''

text = text.replace(old, new)

file.write_text(text, encoding="utf-8")

print("Updated engine/app.js")
