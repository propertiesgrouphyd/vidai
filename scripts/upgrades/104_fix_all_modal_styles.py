from pathlib import Path

file = Path("main.css")

text = file.read_text(encoding="utf-8")

addition = r'''

/* ========================================================================
   VIDHWAAN AI - UNIVERSAL MODAL CARD FIX
   ======================================================================== */


.vw-modal-card{

    width:min(100%,520px);

    background:#ffffff;

    color:#111827;

    border-radius:var(--vw-radius-lg);

    padding:32px;

    display:flex;

    flex-direction:column;

    gap:20px;

    box-shadow:var(--vw-shadow-lg);

    position:relative;

    animation:vw-modal-show .2s ease;

}



.vw-modal-card h2{

    margin:0;

    font-size:24px;

    font-weight:700;

    color:#111827;

}



.vw-modal-card p{

    margin:0;

    color:#6b7280;

    line-height:1.5;

}



.vw-modal-card input{

    width:100%;

    box-sizing:border-box;

    padding:14px 16px;

    border:1px solid #d1d5db;

    border-radius:12px;

    font-size:16px;

    outline:none;

}



.vw-modal-card input:focus{

    border-color:#111827;

}



.vw-modal-actions{

    display:flex;

    gap:12px;

    flex-wrap:wrap;

}



.vw-modal-actions button{

    flex:1;

    min-height:44px;

    padding:12px 18px;

    border:none;

    border-radius:12px;

    cursor:pointer;

    font-size:15px;

    font-weight:600;

}



#vw-save-api-btn,
#vw-payment-btn{

    background:#111827;

    color:#ffffff;

}



#vw-api-link-btn,
#vw-payment-cancel-btn{

    background:#f3f4f6;

    color:#111827;

}



@keyframes vw-modal-show{

    from{

        opacity:0;

        transform:translateY(15px) scale(.98);

    }


    to{

        opacity:1;

        transform:translateY(0) scale(1);

    }

}


'''

if ".vw-modal-card{" not in text:
    text += addition

file.write_text(text, encoding="utf-8")

print("Added universal modal styles")
