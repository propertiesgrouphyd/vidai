from pathlib import Path

file = Path("engine/subscription-manager.js")

text = file.read_text(encoding="utf-8")

# ------------------------------------------------------------------
# Add import
# ------------------------------------------------------------------

import_line = 'import { getUniqueId } from "./identity-manager.js";\n\n'

if "getUniqueId" not in text:
    text = import_line + text

# ------------------------------------------------------------------
# Replace beginning of checkSubscription()
# ------------------------------------------------------------------

old = """async function checkSubscription(uniqueId) {

    if (!uniqueId) {

        return {

            active: false,
            reason: "missing-id"

        };

    }"""

new = """async function checkSubscription(uniqueId) {

    uniqueId =
        uniqueId ||
        getUniqueId();

    if (!uniqueId) {

        return {

            active: false,
            reason: "missing-id"

        };

    }"""

if old not in text:
    print("ERROR: Expected function block not found.")
    exit(1)

text = text.replace(old, new, 1)

file.write_text(text, encoding="utf-8")

print("subscription-manager.js updated successfully.")
