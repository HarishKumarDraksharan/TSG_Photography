document.addEventListener("DOMContentLoaded", function () {
    const hero = document.querySelector(".hero-slideshow");
  
    let index = 0;
    let interval;
  
    function showSlide(i) {
      index = (i + images.length) % images.length;
      hero.style.backgroundImage = `url('${images[index]}')`;
      updateDots();
    }
  
    function nextSlide() {
      showSlide(index + 1);
    }
  
    function prevSlide() {
      showSlide(index - 1);
    }
  
    function startSlideshow() {
      interval = setInterval(nextSlide, 3000);
    }
  
    function updateDots() {
      const dotsContainer = document.getElementById("slideshow-dots");
      dotsContainer.innerHTML = "";
      images.forEach((_, i) => {
        const dot = document.createElement("span");
        dot.style.width = "10px";
        dot.style.height = "10px";
        dot.style.borderRadius = "50%";
        dot.style.display = "inline-block";
        dot.style.backgroundColor = i === index ? "#fff" : "#888";
        dot.style.cursor = "pointer";
        dot.onclick = () => {
          showSlide(i);
          clearInterval(interval);
          startSlideshow();
        };
        dotsContainer.appendChild(dot);
      });
    }
  
    // Expose navigation functions globally
    window.nextSlide = nextSlide;
    window.prevSlide = prevSlide;
  
    showSlide(index);
    startSlideshow();
  });
  