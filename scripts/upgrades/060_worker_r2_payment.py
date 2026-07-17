from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
FILE = ROOT / "worker" / "index.js"

text = FILE.read_text(encoding="utf-8")

# ------------------------------------------------------------------
# Remove OPENAI_API_KEY requirement
# ------------------------------------------------------------------

old = '''requireEnv(env, [
            "OPENAI_API_KEY",
            "RAZORPAY_KEY_ID",
            "RAZORPAY_KEY_SECRET"
        ]);'''

new = '''requireEnv(env, [
            "RAZORPAY_KEY_ID",
            "RAZORPAY_KEY_SECRET"
        ]);'''

if old not in text:
    print("ERROR: requireEnv block not found.")
    sys.exit(1)

text = text.replace(old, new, 1)

# ------------------------------------------------------------------
# Require unique_id
# ------------------------------------------------------------------

old = '''requireFields(data, [
                "razorpay_order_id",
                "razorpay_payment_id",
                "razorpay_signature"
            ]);'''

new = '''requireFields(data, [
                "unique_id",
                "razorpay_order_id",
                "razorpay_payment_id",
                "razorpay_signature"
            ]);'''

if old not in text:
    print("ERROR: verify-payment requireFields block not found.")
    sys.exit(1)

text = text.replace(old, new, 1)

# ------------------------------------------------------------------
# Insert R2 write before success response
# ------------------------------------------------------------------

marker = '''            return json({

                success: true,
'''

insert = '''            await env.R2.put(
                `subscriptions/${data.unique_id}.json`,
                "{}",
                {
                    httpMetadata: {
                        contentType: "application/json"
                    }
                }
            );

''' + marker

if marker not in text:
    print("ERROR: success response marker not found.")
    sys.exit(1)

text = text.replace(marker, insert, 1)

FILE.write_text(text, encoding="utf-8")

print("✓ Worker updated.")
