// Resize logo onscroll
const logoDefault = document.getElementById("logo_default");
const logoNovember = document.getElementById("logo_november");
const logoDecember = document.getElementById("logo_december");

const scrollFunction = () => {
  const scrolled =
    document.body.scrollTop > 50 || document.documentElement.scrollTop > 50;

  const setLogoSize = (logo, width, height) => {
    if (logo) {
      logo.style.width = width;
      logo.style.height = height;
    }
  };

  if (scrolled) {
    setLogoSize(logoDefault, "140px", "71px");
    setLogoSize(logoNovember, "140px", "71px");
    setLogoSize(logoDecember, "140px", "71px");
  } else {
    setLogoSize(logoDefault, "175px", "88px");
    setLogoSize(logoNovember, "175px", "88px");
    setLogoSize(logoDecember, "175px", "88px");
  }
};

window.onscroll = () => {
  scrollFunction();
};

// Tooltip
document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach((el) => {
  new bootstrap.Tooltip(el);
});

// Scroll to certificates
const scrollToAnchor = (aid) => {
  const aTag = document.querySelector("a[name='" + aid + "']");

  if (aTag) {
    window.scrollTo({
      top: aTag.offsetTop,
      behavior: "smooth",
    });
  }
};

document.getElementById("help").addEventListener("click", () => {
  const modal = document.getElementById("Modal6");
  const modalInstance = bootstrap.Modal.getInstance(modal);

  if (modalInstance) {
    modalInstance.hide();
  }

  setTimeout(() => {
    scrollToAnchor("certificates");
  }, 200);
});

// Hide navbar after click when navbar collapsed
const navbarLinks = document.querySelectorAll(".navbar-collapse a");

navbarLinks.forEach((link) => {
  link.addEventListener("click", () => {
    const navbarCollapse = document.querySelector(".navbar-collapse");
    if (navbarCollapse.classList.contains("show")) {
      navbarCollapse.classList.remove("show");
    }
  });
});

// Disable/enable submit form button if captcha is/not verified
function enable() {
  document.getElementById("submitButton").disabled = false;
}

function disable() {
  document.getElementById("submitButton").disabled = true;
}

// AOS animation
AOS.init({
  disable: window.innerWidth < 1399,
  startEvent: "DOMContentLoaded",
  once: true,
  duration: 800,
});
