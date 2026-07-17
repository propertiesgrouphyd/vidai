from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
FILE = ROOT / "worker" / "index.js"

text = FILE.read_text(encoding="utf-8")

marker = """if (!valid) {
    return json(
        {
            success: false,
            error: "Invalid payment signature"
        },
        400
    );
}
"""

if marker not in text:
    print("ERROR: verify-payment marker not found.")
    sys.exit(1)

insert = marker + """

const { unique_id } = data;

if (!unique_id) {
    return json(
        {
            success: false,
            error: "Missing unique_id"
        },
        400
    );
}

const objectKey = `subscriptions/${unique_id}.json`;

await env.R2.put(
    objectKey,
    "{}",
    {
        httpMetadata: {
            contentType: "application/json"
        }
    }
);

"""

text = text.replace(marker, insert, 1)

FILE.write_text(text, encoding="utf-8")

print("✓ R2 subscription support added.")
