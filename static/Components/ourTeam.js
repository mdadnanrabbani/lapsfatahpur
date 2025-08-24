const track = document.querySelector('.carousel-track');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');
let index = 0;

function moveSlide(step) {
  const cardWidth = track.children[0].offsetWidth + 32; // card + gap
  index += step;

  if (index < 0) {
    index = track.children.length - 1;
  } else if (index >= track.children.length) {
    index = 0; // reset back to first card
  }

  track.style.transform = `translateX(-${index * cardWidth}px)`;
}

nextBtn.addEventListener('click', () => moveSlide(1));
prevBtn.addEventListener('click', () => moveSlide(-1));

/* Auto Scroll with Loop */
let autoScroll = setInterval(() => {
  moveSlide(1);
}, 3000); // every 3s

/* Optional: Pause on Hover */
track.addEventListener('mouseenter', () => clearInterval(autoScroll));
track.addEventListener('mouseleave', () => {
  autoScroll = setInterval(() => moveSlide(1), 3000);
});
