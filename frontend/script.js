async function analyze(){
    

let tweet = document.getElementById("tweet").value;

if(tweet===""){

alert("Please enter a tweet");

return;

}

try{

let response = await fetch("http://127.0.0.1:5000/analyze",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
text:tweet
})

});

let data = await response.json();

let score = data.score;

document.getElementById("percent").innerText = score+"%";

let angle = (score/100)*180 - 90;

document.getElementById("needle").style.transform = "rotate("+angle+"deg)";

let emoji="😐";

if(data.sentiment==="Positive") emoji="😊";
if(data.sentiment==="Negative") emoji="😡";

document.getElementById("emoji").innerText = emoji;

let sentimentText = document.getElementById("sentimentText");
let resultBox = document.getElementById("result");

sentimentText.innerText = data.sentiment;

resultBox.className="sentiment-result";

if(data.sentiment==="Positive") resultBox.classList.add("positive");
if(data.sentiment==="Negative") resultBox.classList.add("negative");
if(data.sentiment==="Neutral") resultBox.classList.add("neutral");

}

catch(error){

alert("Backend not connected. Please start Flask server.");

}

}