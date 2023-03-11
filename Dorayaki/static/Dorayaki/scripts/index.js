const interact = (btn) => {
    const audio = document.getElementById("audio-" + btn.id);
    const card = document.getElementById("card-" + btn.id);
    const resetCardAudio = () => {
        card.classList.remove('active');
        btn.classList.remove('clicked');
        btn.innerText = 'Interact';
        audio.pause();
        audio.currentTime = 0;
    }
    audio.addEventListener("ended", function() {
        resetCardAudio();
    })
    if (btn.innerText === 'Stop') {
        resetCardAudio();
    } else {
        card.classList.add('active');
        btn.classList.add('clicked');
        btn.innerText = 'Stop';
        audio.play();
    }
}

function update(e) {
    var x = e.clientX || e.touches[0].clientX
    var y = e.clientY || e.touches[0].clientY
    var offset = document.getElementById(currCard).getBoundingClientRect();
    let xPos = (x - offset.left) / (offset.right - offset.left) * 100 + "%";
    let yPos = (y - offset.top) / (offset.bottom - offset.top) * 100 + "%";
    //console.log("x: " + xPos, "y: " + yPos)
    document.documentElement.style.setProperty('--xPos', xPos)
    document.documentElement.style.setProperty('--yPos', yPos)
}

var currCard = '';

$(document).ready(function() {
    $(".card").hover(function() {
        currCard = $(this).attr('id')
        $(this).addClass("spotlight");
        document.addEventListener('mousemove', update)
        document.addEventListener('touchmove', update)
    }, function() {
        currCard = '';
        $(this).removeClass("spotlight");
        document.removeEventListener('mousemove', update)
        document.removeEventListener('touchmove', update)
    });
});