// Navigation Menu Toggle
const menuBtn = document.getElementById("menu-btn");
const navLinks = document.getElementById("nav-links");
const menuBtnIcon = menuBtn.querySelector("i");

menuBtn.addEventListener("click", () => {
  navLinks.classList.toggle("open");

  const isOpen = navLinks.classList.contains("open");
  menuBtnIcon.setAttribute("class", isOpen ? "ri-close-line" : "ri-menu-line");
});

// Add a scroll event listener to change the navbar style
window.addEventListener('scroll', () => {
  const body = document.body;
  const scrollPosition = window.scrollY; // Current scroll position

  if (scrollPosition > 50) { // Change this value based on when you want the effect
      body.classList.add('scrolled');
  } else {
      body.classList.remove('scrolled');
  }
});

// Close Menu on Click (for mobile)
navLinks.addEventListener("click", () => {
  navLinks.classList.remove("open");
  menuBtnIcon.setAttribute("class", "ri-menu-line");
});

// Scroll Reveal Animations (Using ScrollReveal.js)
const scrollRevealOption = {
  origin: "bottom",
  distance: "50px",
  duration: 1000,
};

// Reveal the Hero Section Elements
ScrollReveal().reveal(".hero__content h1", { ...scrollRevealOption, delay: 200 });
ScrollReveal().reveal(".hero__content p", { ...scrollRevealOption, delay: 400 });
ScrollReveal().reveal(".hero__btns", { ...scrollRevealOption, delay: 600 });
ScrollReveal().reveal(".hero__image img", { ...scrollRevealOption, origin: "right", delay: 800 });

// Reveal the Services Section
ScrollReveal().reveal(".service__card", { ...scrollRevealOption, interval: 300 });

// Reveal the Destination Cards
ScrollReveal().reveal(".destination__card", { ...scrollRevealOption, interval: 300 });

// Reveal Call to Action Banner
ScrollReveal().reveal(".cta-banner h2", { ...scrollRevealOption });
ScrollReveal().reveal(".cta-banner .btn-primary", { ...scrollRevealOption, delay: 200 });
