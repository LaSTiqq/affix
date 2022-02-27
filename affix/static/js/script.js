window.onscroll = function () {
  scrollFunction();
};

const logo_default = document.getElementById("logo_default");
const logo_newy = document.getElementById("logo_newy");
const logo_lv = document.getElementById("logo_lv");
const arrow = document.getElementById("arrow");

function scrollFunction() {
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
}