/**
 * Created by greenman on 6/23/17.
 */
var colorWell
var defaultColor = "#00ff00"

window.addEventListener("load", startup, false);

function startup() {
    colorWell = document.querySelector("#colorWell");
    colorWell.value = defaultColor;
    colorWell.addEventListener("input", updateFirst, false);
    colorWell.addEventListener("change", updateAll, false)
    colorWell.select();

}

function updateFirst(event) {
    var b = document.querySelector("body");

    if(b) {
        b.style.background = event.target.value;
    }

}

function updateAll(event) {
    document.querySelectorAll("body").forEach(function (b) {
        b.style.background = event.target.value;
    })
}