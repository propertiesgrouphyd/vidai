from pathlib import Path

file = Path("engine/ui-manager.js")

text = file.read_text(encoding="utf-8")

text = text.replace(
'''    DropdownManager.populateCategories(
        UI.category
    );

    DropdownManager.populateTopics(
        UI.topic
    );
''',
'''    DropdownManager.clearCategories(
        UI.category
    );

    DropdownManager.clearTopics(
        UI.topic
    );
'''
)

file.write_text(text, encoding="utf-8")

print("Fixed initial category/topic loading")
