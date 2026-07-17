from pathlib import Path

file = Path("engine/app.js")

text = file.read_text(encoding="utf-8")


# Move/add imports at top
imports = '''import { UI, initializeDropdowns, getValues } from "./ui-manager.js";
import { validate } from "./validator.js";
import { save, load } from "./storage.js";
import { buildContext } from "./context-builder.js";
import { buildPrompt } from "./prompt-builder.js";
import { generateContent } from "./ai-client.js";
import * as Output from "./output-renderer.js";
import { ensureApiKey, initializeApiModal } from "./api-manager.js";
import { ensureUniqueId } from "./identity-manager.js";
import { checkSubscription } from "./subscription-manager.js";
import { openPaymentModal, initializePaymentModal } from "./payment-manager.js";

'''

if 'from "./api-manager.js"' not in text:
    start = text.find('"use strict";')

    if start != -1:
        text = text.replace(
            '"use strict";',
            '"use strict";\n\n' + imports,
            1
        )

    # remove duplicate old imports
    old_imports = [
        'import { UI, initializeDropdowns, getValues } from "./ui-manager.js";',
        'import { validate } from "./validator.js";',
        'import { save, load } from "./storage.js";',
        'import { buildContext } from "./context-builder.js";',
        'import { buildPrompt } from "./prompt-builder.js";',
        'import { generateContent } from "./ai-client.js";',
        'import * as Output from "./output-renderer.js";'
    ]

    first_block = text.find('const AI_CONFIG')

    before = text[:first_block]
    after = text[first_block:]

    for item in old_imports:
        after = after.replace(item, "")

    text = before + after


# Insert gate before generateContent
old = '''
        const content = await generateContent(prompt, AI_CONFIG);
'''

new = '''
        if (!ensureApiKey()) {

            return;

        }


        const uniqueId =
            ensureUniqueId();


        const subscription =
            await checkSubscription(uniqueId);


        if (!subscription.active) {

            openPaymentModal();

            return;

        }


        AI_CONFIG.apiKey =
            localStorage.getItem(
                window.VW_CONFIG.STORAGE_KEYS.API_KEY
            );


        const content =
            await generateContent(
                prompt,
                AI_CONFIG
            );
'''

if 'checkSubscription(uniqueId)' not in text:
    text = text.replace(old, new)


# initialize modals
old_init = '''
    initializeDropdowns();

}
'''

new_init = '''
    initializeDropdowns();

    initializeApiModal();

    initializePaymentModal();

}
'''

if 'initializeApiModal();' not in text:
    text = text.replace(old_init, new_init)


file.write_text(text, encoding="utf-8")

print("Generation gate added")
