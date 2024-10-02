window.addEventListener("scroll", () => {
    const navbar = document.querySelector(".navbar");

    const isScrolled = window.scrollY > 0;
    
    if (isScrolled) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled"); 
    }
});
