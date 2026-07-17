from pathlib import Path

file = Path("engine/app.js")
text = file.read_text(encoding="utf-8")

text = text.replace(
'import { save } from "./storage.js";',
'import { save, load } from "./storage.js";'
)

restore_function = '''

function restoreSelections() {

    const values = load();

    for (const [key, value] of Object.entries(values)) {

        if (!value) continue;

        const element = document.querySelector("[data-field='" + key + "']");

        if (element) {

            element.value = value;

        }

    }

}

'''

if "function restoreSelections()" not in text:
    text = text.replace(
        'async function onGenerate() {',
        restore_function + '\nasync function onGenerate() {'
    )

text = text.replace(
'    initializeDropdowns();',
'''    initializeDropdowns();

    restoreSelections();'''
)

file.write_text(text, encoding="utf-8")

print("Updated engine/app.js")
