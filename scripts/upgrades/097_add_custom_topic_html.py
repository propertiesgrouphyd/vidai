from pathlib import Path

file = Path("index.html")

text = file.read_text(encoding="utf-8")

marker = '''
                        <div class="vw-field">

                            <label for="vw-goal">
'''

insert = '''
                        <div
                            class="vw-field"
                            id="vw-custom-topic-wrapper"
                            hidden>

                            <label for="vw-custom-topic">

                                Custom Topic

                            </label>

                            <input
                                id="vw-custom-topic"
                                name="customTopic"
                                type="text"
                                maxlength="100"
                                placeholder="Enter custom topic (max 100 characters)">

                        </div>


'''

if "vw-custom-topic-wrapper" not in text:

    if marker not in text:
        raise Exception("Insertion point not found")

    text = text.replace(
        marker,
        insert + marker
    )

file.write_text(text, encoding="utf-8")

print("Custom topic HTML added")
