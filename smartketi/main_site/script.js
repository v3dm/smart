const slider = document.querySelector('.slider');
const slides = document.querySelectorAll('.slide');
const prevArrow = document.querySelector('.prev');
const nextArrow = document.querySelector('.next');
const dots = document.querySelectorAll('.dot');

let currentIndex = 0;
const totalSlides = slides.length;

function updateSlider() {
    slider.style.transform = `translateX(-${currentIndex * 100}%)`;
    dots.forEach((dot, index) => {
        dot.classList.toggle('active', index === currentIndex);
    });
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % totalSlides;
    updateSlider();
}

function prevSlide() {
    currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
    updateSlider();
}

// Arrow controls
nextArrow.addEventListener('click', nextSlide);
prevArrow.addEventListener('click', prevSlide);

// Dot controls
dots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
        currentIndex = index;
        updateSlider();
    });
});

// Auto-advance
let autoSlide = setInterval(nextSlide, 5000);

// Pause on hover
slider.parentElement.addEventListener('mouseenter', () => {
    clearInterval(autoSlide);
});

slider.parentElement.addEventListener('mouseleave', () => {
    autoSlide = setInterval(nextSlide, 5000);
});

// ... ... ... ...   ...
document.addEventListener('DOMContentLoaded', function() {
  particlesJS('particles-bg', {
    "particles": {
      "number": {
        "value": 50,
        "density": {
          "enable": true,
          "value_area": 800
        }
      },
      "color": {
        "value": "#0077b6" // Brand color
      },
      "shape": {
        "type": "circle",
        "stroke": {
          "width": 0,
          "color": "#000000"
        }
      },
      "opacity": {
        "value": 0.5,
        "random": true,
        "anim": {
          "enable": true,
          "speed": 1.5,
          "opacity_min": 0.1,
          "sync": false
        }
      },
      "size": {
        "value": 4,
        "random": true,
        "anim": {
          "enable": false
        }
      },
      "line_linked": {
        "enable": true,
        "distance": 150,
        "color": "#00b4d8", // Secondary color
        "opacity": 0.4,
        "width": 1
      },
      "move": {
        "enable": true,
        "speed": 1,
        "direction": "none",
        "random": true,
        "straight": false,
        "out_mode": "out",
        "bounce": false
      }
    },
    "retina_detect": true
  });
});