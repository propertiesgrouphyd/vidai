from pathlib import Path

file = Path("engine/dropdown-manager.js")

text = file.read_text(encoding="utf-8")

old = '''
    populateTopics(select) {
        populateSelect(select, DataManager.getTopics(), "Select Topic");
    },
'''

new = '''
    populateTopics(select) {

        const topics = [
            ...DataManager.getTopics(),
            {
                id: "custom-topic",
                label: "Custom Topic"
            }
        ];

        populateSelect(
            select,
            topics,
            "Select Topic"
        );

    },
'''

text = text.replace(old, new)

file.write_text(text, encoding="utf-8")

print("Custom topic option added")
