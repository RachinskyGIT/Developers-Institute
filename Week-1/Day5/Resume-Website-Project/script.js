
// Mango rotation animation script
$(document).ready(function () {
    $(".stas-spin").on("animationiteration", function () {
      $(this).removeClass("animated");
      console.log("out");
    });
  
    $(".stas-spin").hover(function () {
      $(this).addClass("animated");
      console.log("over");
    });
  });