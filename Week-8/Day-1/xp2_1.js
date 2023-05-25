// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will alert “Hello World”.
function setTime(){
    setTimeout(function(){
      alert('Hello, world!');
    },2000)
  }


// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
setTimeout(function() {
    var container = document.getElementById("container");
    var paragraph = document.createElement("p");
    paragraph.textContent = "Hello World";
    container.appendChild(paragraph);
  }, 2000);


// In your Javascript file, using setInterval, call a function every 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// The interval will be cleared (ie. clearInterval), when the user will click on the button.
// Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will 
// be 5 paragraphs inside the <div id="container">.
var container = document.getElementById("container");
var interval = setInterval(function() {
    var paragraphs = container.getElementsByTagName("p");
    var paragraph = document.createElement("p");
    paragraph.textContent = "Hello World";
    container.appendChild(paragraph);
    if (paragraphs.length === 5) {
      clearInterval(interval);
    }
}, 2000);

var button = document.getElementById("clear");
button.addEventListener("click", function() {
  clearInterval(interval);
});
