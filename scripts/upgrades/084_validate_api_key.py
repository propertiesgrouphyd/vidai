from pathlib import Path

file = Path("engine/ai-client.js")

text = file.read_text(encoding="utf-8")

old = '''
    if (!prompt) {

        throw new Error("Prompt is required.");

    }
'''

new = '''
    if (!prompt) {

        throw new Error("Prompt is required.");

    }


    if (!config.apiKey) {

        throw new Error("API key not configured.");

    }
'''

if "API key not configured" not in text:
    text = text.replace(old, new)

file.write_text(text, encoding="utf-8")

print("API key validation added")
