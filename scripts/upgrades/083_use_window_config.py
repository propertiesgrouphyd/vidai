from pathlib import Path

file = Path("engine/app.js")

text = file.read_text(encoding="utf-8")

text = text.replace(
    "VW_CONFIG.API.BASE_URL",
    "window.VW_CONFIG.API.BASE_URL"
)

text = text.replace(
    "VW_CONFIG.API.CHAT_ENDPOINT",
    "window.VW_CONFIG.API.CHAT_ENDPOINT"
)

text = text.replace(
    "VW_CONFIG.STORAGE_KEYS.API_KEY",
    "window.VW_CONFIG.STORAGE_KEYS.API_KEY"
)

text = text.replace(
    "VW_CONFIG.API.MODEL",
    "window.VW_CONFIG.API.MODEL"
)

file.write_text(text, encoding="utf-8")

print("Updated app.js config access")
