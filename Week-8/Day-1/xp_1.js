// Set page to Dark-mode
document.body.style.background = "#4E6C84";


// Using a DOM property, retrieve the h1 and console.log it.
var h1Text = document.querySelector("h1").textContent;
console.log(h1Text)


// Using DOM methods, remove the last paragraph in the <article> tag.
var articleItems = document.querySelectorAll("article p:last-of-type");
articleItems.forEach(function(item) {
  item.parentNode.removeChild(item);
});

// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.
let items_h2 = document.querySelectorAll("h2");
items_h2.forEach(function(item) {
  item.addEventListener("click", function() {
    this.style.background = "lightblue";
  });
});

// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).
let items_h3 = document.querySelectorAll("h3");
items_h3.forEach(function(item) {
  item.addEventListener("click", function() {
    item.style.display = "none";
  });
});


// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
var container = document.body;
var btn = document.createElement('button');
btn.textContent = 'To Bold';

btn.addEventListener("click", function(){
    document.querySelectorAll('article *').forEach(function(element) { // Select all elements in the article
        element.style.fontWeight = 'bold'; 
      });
});
// Add button to page
container.appendChild(btn);



// BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100
function getRandomPixelValue(min, max) {
  var randomNum = Math.floor(Math.random() * (max - min + 1)) + min;
  return randomNum + "px";
}
var randomPixel = getRandomPixelValue(1, 100);


let items_h1 = document.querySelectorAll("h1");
items_h1.forEach(function(item) {
  item.addEventListener("mouseover", function() {
    this.style.fontSize = randomPixel;
  });
});

// BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)
var articleItems = document.querySelectorAll("article p:nth-of-type(2)");
articleItems.forEach(function(item) {
  item.addEventListener("mouseover", function() {
    this.style.transition = "opacity 1s";
    this.style.opacity = "0";
  });
});




