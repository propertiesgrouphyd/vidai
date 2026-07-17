from pathlib import Path

file = Path("engine/ui-manager.js")

text = file.read_text(encoding="utf-8")


# 1. Add custom topic UI reference
old = '''
    topic: document.getElementById("vw-topic"),
'''

new = '''
    topic: document.getElementById("vw-topic"),

    customTopic:
        document.getElementById("vw-custom-topic"),
'''

if "customTopic:" not in text:
    text = text.replace(old, new)


# 2. Add topic custom listener
listener = '''

    if (UI.topic) {

        UI.topic.addEventListener(
            "change",
            () => {

                const wrapper =
                    document.getElementById(
                        "vw-custom-topic-wrapper"
                    );

                if (!wrapper) return;


                if (UI.topic.value === "custom-topic") {

                    wrapper.hidden = false;

                } else {

                    wrapper.hidden = true;

                    if (UI.customTopic) {

                        UI.customTopic.value = "";

                    }

                }

            }
        );

    }

'''

if "vw-custom-topic-wrapper" not in text:
    text = text.replace(
        '''
    if (UI.category) {
''',
        listener + '''
    if (UI.category) {
'''
    )


# 3. Update getValues topic handling
old_topic = '''
        topic: UI.topic?.value || "",
'''

new_topic = '''
        topic:
            UI.topic?.value === "custom-topic"
                ? UI.customTopic?.value || ""
                : UI.topic?.value || "",

        customTopic:
            UI.customTopic?.value || "",
'''

if "customTopic:" not in text.split("function getValues()")[1]:
    text = text.replace(old_topic, new_topic)


file.write_text(text, encoding="utf-8")

print("Custom topic UI connected")
