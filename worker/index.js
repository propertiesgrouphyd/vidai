const SUBSCRIPTION_DAYS = 30;
const AMOUNT = 3000; // ₹30


export default {

async fetch(request, env) {


    if (request.method === "OPTIONS") {
        return cors();
    }


    const url = new URL(request.url);


    try {


        if (
            request.method === "POST" &&
            url.pathname === "/create-order"
        ) {

            return await createOrder(
                request,
                env
            );

        }



        if (
            request.method === "POST" &&
            url.pathname === "/verify-payment"
        ) {

            return await verifyPayment(
                request,
                env
            );

        }



        return json(
            {
                error:"Not Found"
            },
            404
        );


    } catch(error) {


        return json(
            {
                error:error.message
            },
            500
        );


    }


}

};





function json(
    data,
    status = 200
){

return new Response(

JSON.stringify(data),

{

status,

headers:{

"Content-Type":
"application/json",

"Access-Control-Allow-Origin":
"*",

"Access-Control-Allow-Methods":
"POST, OPTIONS",

"Access-Control-Allow-Headers":
"Content-Type"

}

}

);

}






function cors(){

return new Response(
null,
{

status:204,

headers:{

"Access-Control-Allow-Origin":"*",

"Access-Control-Allow-Methods":
"POST, OPTIONS",

"Access-Control-Allow-Headers":
"Content-Type"

}

}

);

}








async function createOrder(
request,
env
){


const body =
await request.json();



const uniqueId =
body.uniqueId;



if(!uniqueId){

return json(
{
error:"Unique ID required"
},
400
);

}




const auth =
btoa(
`${env.RAZORPAY_KEY_ID}:${env.RAZORPAY_KEY_SECRET}`
);




const response =
await fetch(

"https://api.razorpay.com/v1/orders",

{

method:"POST",

headers:{

"Authorization":
`Basic ${auth}`,

"Content-Type":
"application/json"

},

body:JSON.stringify({

amount:AMOUNT,

currency:"INR",

receipt:
`VIDHWAAN-${Date.now()}`

})

}

);





if(!response.ok){

throw new Error(
"Razorpay order creation failed"
);

}




const order =
await response.json();





/*
    Store temporary order mapping

    Prevents:
    User A payment
    User B uniqueId activation

*/


await env.SUBSCRIPTIONS.put(

`orders/${order.id}.json`,

JSON.stringify({

orderId:
order.id,

uniqueId,

created:
Date.now()

}),

{

httpMetadata:{

contentType:
"application/json"

}

}

);







return json({

success:true,

key:
env.RAZORPAY_KEY_ID,

orderId:
order.id,

amount:
AMOUNT

});

}

async function verifyPayment(
    request,
    env
){


const body =
await request.json();



const {

paymentId,

orderId,

signature,

uniqueId


} = body;




if(
!paymentId ||
!orderId ||
!signature ||
!uniqueId
){

return json(
{
error:"Missing payment details"
},
400
);

}






const valid =
await verifySignature(

orderId,

paymentId,

signature,

env.RAZORPAY_KEY_SECRET

);





if(!valid){

return json(
{
error:"Invalid payment signature"
},
403
);

}






/*
    Check order ownership

    orderId
        ↓
    stored uniqueId
*/


const orderData =
await env.SUBSCRIPTIONS.get(

`orders/${orderId}.json`

);




if(!orderData){

return json(
{
error:"Order not found"
},
404
);

}





const order =
await orderData.json();





if(
order.uniqueId !== uniqueId
){

return json(
{
error:"Unique ID mismatch"
},
403
);

}






/*
    Create subscription
*/


const expires =

Date.now()
+
(
SUBSCRIPTION_DAYS *
24 *
60 *
60 *
1000
);






const subscription = {


uniqueId,


plan:
"30-days",


paymentId,


orderId,


created:
Date.now(),


expires


};






await env.SUBSCRIPTIONS.put(

`${uniqueId}.json`,

JSON.stringify(subscription),

{

httpMetadata:{

contentType:
"application/json"

}

}

);

try {
    await purgeSubscription(env, uniqueId);
} catch (err) {
    console.error("Cache purge failed:", err);
}





/*
    Remove temporary order
*/


await env.SUBSCRIPTIONS.delete(

`orders/${orderId}.json`

);






return json({

success:true,

uniqueId,

expires

});


}

async function verifySignature(
orderId,
paymentId,
signature,
secret
){


const encoder =
new TextEncoder();




const key =
await crypto.subtle.importKey(

"raw",

encoder.encode(secret),

{

name:"HMAC",

hash:"SHA-256"

},

false,

["sign"]

);





const signed =
await crypto.subtle.sign(

"HMAC",

key,

encoder.encode(

`${orderId}|${paymentId}`

)

);





const expected =

[
...new Uint8Array(signed)
]

.map(

b =>
b
.toString(16)
.padStart(2,"0")

)

.join("");





return expected === signature;


}
async function purgeSubscription(
    env,
    uniqueId
){

const url =

`https://api.cloudflare.com/client/v4/zones/${env.CF_ZONE_ID}/purge_cache`;



const response =

await fetch(

url,

{

method:"POST",

headers:{

"Authorization":
`Bearer ${env.CF_API_TOKEN}`,

"Content-Type":
"application/json"

},

body:JSON.stringify({

files:[
    `https://subscriptions.propertiesgrouphyd.online/subscriptions/${uniqueId}.json`
]

})

}

);





if(!response.ok){

const error =
await response.text();


throw new Error(
"Cache purge failed: " + error
);

}




return true;


}

