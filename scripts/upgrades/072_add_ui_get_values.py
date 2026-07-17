from pathlib import Path

FILE = Path("engine/ui-manager.js")

text = FILE.read_text()

old = """
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
"""

new = old + """

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
"""

if "function getValues()" not in text:
    text = text.replace(old, new)

text = text.replace(
"""export {

    UI,

    initializeDropdowns

};""",
"""export {

    UI,

    initializeDropdowns,

    getValues

};"""
)

FILE.write_text(text)

print("Updated engine/ui-manager.js")
