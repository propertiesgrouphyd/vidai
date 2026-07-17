from pathlib import Path

file = Path("engine/dropdown-manager.js")

text = file.read_text(encoding="utf-8")

insert = '''

    clearCategories(select) {

        populateSelect(
            select,
            [],
            "Select Category"
        );

    },


    clearTopics(select) {

        populateSelect(
            select,
            [],
            "Select Topic"
        );

    },

'''

marker = '''
    populateCategoriesByPurpose(select, purpose) {
'''

if "clearCategories" not in text:
    text = text.replace(marker, insert + marker)

file.write_text(text, encoding="utf-8")

print("Added empty dropdown handlers")
