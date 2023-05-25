function myMove() {
    var container = document.getElementById("container");
    var animate = document.getElementById("animate");
    
    var position = 0;
    var intervalId = setInterval(frame, 1);
    
    function frame() {
      if (position === container.offsetWidth - animate.offsetWidth) {
        clearInterval(intervalId);
      } else {
        position++;
        animate.style.left = position + "px";
      }
    }
  }
  