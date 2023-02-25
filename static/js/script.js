const logo_default = document.getElementById("logo_default");
const logo_lv = document.getElementById("logo_lv");
const logo_newy = document.getElementById("logo_newy");
const arrow = document.getElementById("arrow");

const scrollFunction = () => {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    arrow.style.display = "block";
    // End values
    if (logo_default) {
      logo_default.style.width = "110px";
      logo_default.style.height = "60px";
    }
    if (logo_newy) {
      logo_newy.style.width = "115px";
      logo_newy.style.height = "73px";
    }
    if (logo_lv) {
      logo_lv.style.width = "110px";
      logo_lv.style.height = "60px";
    }
  } else {
    arrow.style.display = "none";
    // Start values
    if (logo_default) {
      logo_default.style.width = "160px";
      logo_default.style.height = "80px";
    }
    if (logo_newy) {
      logo_newy.style.width = "165px";
      logo_newy.style.height = "95px";
    }
    if (logo_lv) {
      logo_lv.style.width = "160px";
      logo_lv.style.height = "80px";
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

// Scroll to certs
function scrollToAnchor(aid) {
  let aTag = $("a[name='" + aid + "']");
  $("html,body").animate({ scrollTop: aTag.offset().top }, "slow");
}

$("#help").click(function () {
  $("#Modal6").modal("hide");
  scrollToAnchor("certificates");
});

// Hide navbar after click
$(".navbar-collapse a").click(function () {
  $(".navbar-collapse").collapse("hide");
});
