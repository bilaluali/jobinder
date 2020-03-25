
var i = 0;
var txt = 'Looking to Post a JobOffer?';
var speed = 150;

function typeWriterEffect() {
    if (i < txt.length) {
        document.getElementById("text-writer").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWriterEffect, speed);
    } else {
        i = 0;
        document.getElementById("text-writer").innerHTML = "";
        typeWriterEffect();
    }
}

window.onload = typeWriterEffect;