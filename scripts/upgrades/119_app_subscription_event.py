from pathlib import Path

f=Path("engine/app.js")

text=f.read_text()

marker="""document.addEventListener("DOMContentLoaded", () => {"""

insert="""document.addEventListener(

    "vw-subscription-activated",

    () => {

        onGenerate();

    }

);


"""

if insert not in text:
    text=text.replace(marker,insert+marker,1)

f.write_text(text)

print("app.js updated")
