const logoDefault = document.getElementById("logo_default");
const logoNovember = document.getElementById("logo_november");
const logoJanuary = document.getElementById("logo_january");
const arrow = document.getElementById("arrow");

const scrollFunction = () => {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    // End values
    arrow.style.display = "block";
    if (logoDefault) {
      logoDefault.style.width = "130px";
      logoDefault.style.height = "70px";
    }
    if (logoNovember) {
      logoNovember.style.width = "130px";
      logoNovember.style.height = "70px";
    }
    if (logoJanuary) {
      logoJanuary.style.width = "140px";
      logoJanuary.style.height = "80px";
    }
  } else {
    // Start values
    arrow.style.display = "none";
    if (logoDefault) {
      logoDefault.style.width = "160px";
      logoDefault.style.height = "80px";
    }
    if (logoNovember) {
      logoNovember.style.width = "160px";
      logoNovember.style.height = "80px";
    }
    if (logoJanuary) {
      logoJanuary.style.width = "170px";
      logoJanuary.style.height = "90px";
    }
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
