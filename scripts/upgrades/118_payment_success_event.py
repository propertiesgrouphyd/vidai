from pathlib import Path

f = Path("engine/payment-manager.js")

text = f.read_text()

old = """                            if(result.success){

                                closePaymentModal();


                                window.location.reload();

                            }"""

new = """                            if(result.success){

                                closePaymentModal();

                                document.dispatchEvent(

                                    new CustomEvent(

                                        "vw-subscription-activated",

                                        {

                                            detail:result

                                        }

                                    )

                                );

                            }"""

if old not in text:
    print("Target block not found")
    raise SystemExit(1)

text = text.replace(old,new,1)

f.write_text(text)

print("payment-manager updated")
