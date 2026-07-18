from pathlib import Path

file = Path("index.html")

text = file.read_text(encoding="utf-8")

sdk = '<script src="https://checkout.razorpay.com/v1/checkout.js"></script>'

if sdk in text:
    print("Razorpay SDK already exists")
    exit()

marker = '<script type="module" src="engine/app.js"></script>'

if marker not in text:
    print("ERROR: app.js module marker not found")
    exit(1)

text = text.replace(
    marker,
    sdk + "\n\n" + marker,
    1
)

file.write_text(text, encoding="utf-8")

print("Razorpay SDK added")
