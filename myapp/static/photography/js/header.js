
document.addEventListener("DOMContentLoaded", function () {
  const header = document.querySelector("header");
  const nav = document.querySelector("nav");

  window.addEventListener("scroll", function () {
    if (window.scrollY > 50) {
      header.classList.add("py-smaller");
      header.classList.remove("py-large");
    } else {
      header.classList.remove("py-smaller");
      header.classList.add("py-large");
    }
  });
});
