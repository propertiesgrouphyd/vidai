from pathlib import Path

file = Path("engine/dropdown-manager.js")

text = file.read_text(encoding="utf-8")

insert = '''

    populateCategoriesByPurpose(select, purpose) {

        const categories =
            DataManager.getCategoriesByPurpose(purpose);

        populateSelect(
            select,
            categories,
            "Select Category"
        );

    },


    populateTopicsByCategory(select, category) {

        const topics =
            DataManager.getTopicsByCategory(category);

        populateSelect(
            select,
            topics,
            "Select Topic"
        );

    },

'''

marker = '''
    populateCategories(select) {
'''

if "populateCategoriesByPurpose" not in text:
    text = text.replace(marker, insert + marker)

file.write_text(text, encoding="utf-8")

print("Added filtered dropdown methods")
