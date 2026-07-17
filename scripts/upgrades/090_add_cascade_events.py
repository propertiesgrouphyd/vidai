from pathlib import Path

file = Path("engine/ui-manager.js")

text = file.read_text(encoding="utf-8")


# Replace initial category/topic loading
text = text.replace(
'''
    DropdownManager.populateCategories(UI.category);

    DropdownManager.populateTopics(UI.topic);
''',
'''
    DropdownManager.populateCategories(
        UI.category
    );

    DropdownManager.populateTopics(
        UI.topic
    );
'''
)


# Add cascade function before getValues
insert = '''

function initializeCascadeDropdowns() {

    if (UI.purpose) {

        UI.purpose.addEventListener(
            "change",
            () => {

                DropdownManager.populateCategoriesByPurpose(
                    UI.category,
                    UI.purpose.value
                );

                DropdownManager.populateTopicsByCategory(
                    UI.topic,
                    ""
                );

            }
        );

    }


    if (UI.category) {

        UI.category.addEventListener(
            "change",
            () => {

                DropdownManager.populateTopicsByCategory(
                    UI.topic,
                    UI.category.value
                );

            }
        );

    }

}


'''

if "function initializeCascadeDropdowns()" not in text:
    text = text.replace(
        "function getValues()",
        insert + "function getValues()"
    )


# Call cascade after normal initialization
text = text.replace(
'''
    DropdownManager.populateCTAs(UI.cta);

}
''',
'''
    DropdownManager.populateCTAs(UI.cta);

    initializeCascadeDropdowns();

}
'''
)


file.write_text(text, encoding="utf-8")

print("Added cascading dropdown events")
