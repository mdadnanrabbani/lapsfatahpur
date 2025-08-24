const carousel = document.getElementById("newsCarousel");

let scrollAmount = 0;
setInterval(() => {
  if (scrollAmount >= carousel.scrollWidth - carousel.clientWidth) {
    scrollAmount = 0;
  } else {
    scrollAmount += 340; // Card width + gap
  }
  carousel.scrollTo({
    left: scrollAmount,
    behavior: "smooth"
  });
}, 3000); // Auto-scroll every 3s
