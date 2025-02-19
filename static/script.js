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

  function toggleDarkMode() {
    document.documentElement.classList.toggle('dark'); // Pakai documentElement agar Tailwind mendeteksi
    const isDark = document.documentElement.classList.contains('dark');

    localStorage.setItem('theme', isDark ? 'dark' : 'light');

    // Ubah ikon berdasarkan mode
    document.getElementById('theme-icon').className = isDark ? 'fas fa-moon' : 'fas fa-sun';
  }

  document.addEventListener('DOMContentLoaded', () => {
    if (localStorage.getItem('theme') === 'dark') {
      document.documentElement.classList.add('dark');
      document.getElementById('theme-icon').className = 'fas fa-moon';
    } else {
      document.documentElement.classList.remove('dark');
      document.getElementById('theme-icon').className = 'fas fa-sun';
    }
  });