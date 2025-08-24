// JavaScript (Scroll Animation Trigger)
document.addEventListener("DOMContentLoaded", function () {
  const aboutSection = document.querySelector(".about-container");

  function revealOnScroll() {
    const sectionTop = aboutSection.getBoundingClientRect().top;
    const triggerPoint = window.innerHeight - 100;

    if (sectionTop < triggerPoint) {
      aboutSection.style.opacity = "1";
    }
  }

  window.addEventListener("scroll", revealOnScroll);
});
