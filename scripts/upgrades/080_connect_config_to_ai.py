from pathlib import Path

file = Path("engine/app.js")

text = file.read_text(encoding="utf-8")

config_block = '''

const AI_CONFIG = {

    baseUrl:
        VW_CONFIG.API.BASE_URL +
        VW_CONFIG.API.CHAT_ENDPOINT,

    apiKey:
        localStorage.getItem(
            VW_CONFIG.STORAGE_KEYS.API_KEY
        ),

    model:
        VW_CONFIG.API.MODEL,

    temperature: 0.7,

    maxTokens: 4096

};

'''

if "const AI_CONFIG" not in text:
    text = text.replace(
        '"use strict";',
        '"use strict";\\n\\n' + config_block
    )

text = text.replace(
    'await generateContent(prompt);',
    'await generateContent(prompt, AI_CONFIG);'
)

file.write_text(text, encoding="utf-8")

print("Connected VW_CONFIG to AI client")
