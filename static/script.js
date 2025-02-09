document.addEventListener("DOMContentLoaded", function () {
  const menuButton = document.getElementById("menu-button");
  const mobileMenu = document.getElementById("mobile-menu");
  const menuIconOpen = document.getElementById("menu-icon-open");
  const menuIconClose = document.getElementById("menu-icon-close");

  menuButton.addEventListener("click", function () {
    mobileMenu.classList.toggle("hidden");
    menuIconOpen.classList.toggle("hidden");
    menuIconClose.classList.toggle("hidden");
  });
});

document.getElementById('contactForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Mencegah reload halaman
    showModal(); // Tampilkan modal sukses

    // Reset form setelah pesan terkirim
    document.getElementById('contactForm').reset();
  });

  function showModal() {
    document.getElementById('successModal').classList.remove('hidden');
  }

  function closeModal() {
    document.getElementById('successModal').classList.add('hidden');
  }