from pathlib import Path

file = Path("engine/app.js")
text = file.read_text(encoding="utf-8")

text = text.replace(
'import { initializeDropdowns, getValues } from "./ui-manager.js";',
'import { UI, initializeDropdowns, getValues } from "./ui-manager.js";'
)

start = text.find("function restoreSelections() {")
if start != -1:
    brace = 0
    end = start
    while end < len(text):
        if text[end] == "{":
            brace += 1
        elif text[end] == "}":
            brace -= 1
            if brace == 0:
                end += 1
                break
        end += 1

    new_func = '''function restoreSelections() {

    const values = load();

    if (!values) return;

    const map = {

        purpose: UI.purpose,
        category: UI.category,
        topic: UI.topic,
        goal: UI.goal,
        contentStyle: UI.contentStyle,
        audience: UI.audience,
        length: UI.length,
        platform: UI.platform,
        language: UI.language,
        creativity: UI.creativity,
        emoji: UI.emoji,
        cta: UI.cta

    };

    for (const [key, element] of Object.entries(map)) {

        if (element && values[key] !== undefined) {

            element.value = values[key];

        }

    }

}
'''

    text = text[:start] + new_func + text[end:]

file.write_text(text, encoding="utf-8")

print("restoreSelections() updated")
