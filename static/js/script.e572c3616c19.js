// Resize logo onscroll
const logoDefault = document.getElementById("logo_default");
const logoNovember = document.getElementById("logo_november");
const logoDecember = document.getElementById("logo_december");

const scrollFunction = () => {
    const scrolled = document.body.scrollTop > 50 || document.documentElement.scrollTop > 50;

    const setLogoSize = (logo, width, height) => {
      if (logo) {
        logo.style.width = width;
        logo.style.height = height;
      }
    };

    if (scrolled) {
      setLogoSize(logoDefault, "130px", "70px");
      setLogoSize(logoNovember, "130px", "70px");
      setLogoSize(logoDecember, "145px", "85px");
    } else {
      setLogoSize(logoDefault, "160px", "80px");
      setLogoSize(logoNovember, "160px", "80px");
      setLogoSize(logoDecember, "175px", "95px");
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
function scrollToAnchor(aid) {
  let aTag = $("a[name='" + aid + "']");
  $("html,body").animate({ scrollTop: aTag.offset().top }, "slow");
}

$("#help").click(function () {
  $("#Modal6").modal("hide");
  scrollToAnchor("certificates");
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
