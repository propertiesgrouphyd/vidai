from pathlib import Path

file = Path("engine/data-manager.js")

text = file.read_text(encoding="utf-8")

insert = '''

    getCategoriesByPurpose(purpose) {

        return data.categories.filter(

            item => item.purpose === purpose

        );

    },


    getTopicsByCategory(category) {

        return data.topics.filter(

            item => item.category === category

        );

    },

'''

marker = '''
    getCategory(id) {
'''

if "getCategoriesByPurpose" not in text:
    text = text.replace(marker, insert + marker)

file.write_text(text, encoding="utf-8")

print("Added category/topic filtering")
