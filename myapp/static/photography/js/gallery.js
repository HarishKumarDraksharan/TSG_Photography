document.addEventListener("DOMContentLoaded", function () {
    const galleryItems = document.querySelectorAll(".gallery-item");
    const container = document.querySelector(".gallery-container");
  
    function updateCenter() {
      galleryItems.forEach((item) => item.classList.remove("center"));
      const containerCenter = container.offsetWidth / 2;
  
      let closestItem = null;
      let closestDistance = Infinity;
  
      galleryItems.forEach((item) => {
        const rect = item.getBoundingClientRect();
        const itemCenter = rect.left + rect.width / 2;
        const distance = Math.abs(containerCenter - itemCenter);
        if (distance < closestDistance) {
          closestDistance = distance;
          closestItem = item;
        }
      });
  
      if (closestItem) closestItem.classList.add("center");
    }
  
    function animate() {
      updateCenter();
      requestAnimationFrame(animate);
    }
  
    animate();
  });
  