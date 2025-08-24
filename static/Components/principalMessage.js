document.addEventListener("DOMContentLoaded", function () {
    const section = document.querySelector(".principal-message");

    function checkVisibility() {
        const rect = section.getBoundingClientRect();
        if (rect.top < window.innerHeight - 100) {
            section.classList.add("show");
            window.removeEventListener("scroll", checkVisibility);
        }
    }

    window.addEventListener("scroll", checkVisibility);
    checkVisibility();
});
