let list = document.querySelector('.slider .list');
let items = document.querySelectorAll('.slider .list .item');
let dots = document.querySelectorAll('.slider .dots li');
let prev = document.getElementById('prev');
let next = document.getElementById('next');

let active = 0;
let lengthItems = items.length - 1;
let refreshSlider;

function reloadSlider() {
    let checkLeft = items[active].offsetLeft;
    list.style.transition = "left 1s ease-in-out";
    list.style.left = -checkLeft + 'px';

    let lastActiveDot = document.querySelector('.slider .dots li.active');
    if (lastActiveDot) lastActiveDot.classList.remove('active');
    dots[active].classList.add('active');

    clearInterval(refreshSlider);
    refreshSlider = setInterval(() => {
        next.click();
    }, 5000);
}

next.onclick = function() {
    if (active + 1 > lengthItems) {
        active = 0;
    } else {
        active += 1;
    }
    reloadSlider();
};

prev.onclick = function() {
    if (active - 1 < 0) {
        active = lengthItems;
    } else {
        active -= 1;
    }
    reloadSlider();
};

refreshSlider = setInterval(() => {
    next.click();
}, 5000);

dots.forEach((li, key) => {
    li.addEventListener('click', function() {
        active = key;
        reloadSlider();
    });
});

reloadSlider();
