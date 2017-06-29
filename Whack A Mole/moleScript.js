/**
 * Created by greenman on 6/29/17.
 */
$('.hole').html("<img src='images/hole.jpg' />");


function randomHole() {
    var hole = Math.floor(Math.random() * 100) % 20 +1;
    console.log(hole);
    return '#' + hole;
}

function randomAlien() {
    var alienNumber = Math.floor(Math.random() * 10) % 3 +1;
    var alien;
    if (alienNumber === 1){alien = "<img src='images/alienintophat.png'/>" ;};
    if (alienNumber === 2){alien= "<img src='images/alien.png'/>"};
    if (alienNumber === 3){alien = "<img src='images/tokingalien.png'/>"};

    return alien;
}

var timer;
var interval = 3000;

$('#start').click(function()
{
    timer = setInterval(function () {

        var alien = randomAlien();
        var hole = randomHole();
        console.log(alien);
        console.log(hole);
        $(hole).html(alien)
    }, interval);
});

$("#stop").click(function () {
    clearInterval(timer);
});

