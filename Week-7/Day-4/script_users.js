// ex5

// Log the updated HTML content
var containerDiv = document.getElementById("container");
console.log(containerDiv.innerHTML);


// Retrieve the <li> elements within the first <ul> with class "list"
var listItems = document.querySelectorAll("ul.list:nth-of-type(1) li");

// Iterate over the <li> elements to find and remove the one containing "Sarah"
for (var i = 0; i < listItems.length; i++) {
    if (listItems[i].textContent === "Pete") {
        listItems[i].textContent = "Richard";
        break; 
    }
}



// Retrieve the <li> elements within the second <ul> with class "list"
var listItems = document.querySelectorAll("ul.list:nth-of-type(2) li");

// Iterate over the <li> elements to find and remove the one containing "Sarah"
for (var i = 0; i < listItems.length; i++) {
    if (listItems[i].textContent === "Sarah") {
        listItems[i].parentNode.removeChild(listItems[i]);
        break; 
    }
}



// Add the class "student_list" to both <ul> elements
var ulElements = document.querySelectorAll("ul.list");
ulElements.forEach(function(ul) {
    ul.classList.add("student_list");
});

// Add the classes "university" and "attendance" to the first <ul>
var firstUl = document.querySelector("ul.list:first-of-type");
firstUl.classList.add("university", "attendance");



// add bacground color and padding to the "div" container
let item = document.getElementById("container");
item.style.background = "lightblue";
item.style.padding = "10px";


// Hide the <li> containing the text node "Dan"
var liElement = document.querySelector("ul.list:last-of-type li:last-of-type");
liElement.style.display = "none";



// Retrieve the <li> elements within the second <ul> with class "list"
var listItems = document.querySelectorAll("ul li");

// Iterate over the <li> elements to find and remove the one containing "Sarah"
for (var i = 0; i < listItems.length; i++) {
    if (listItems[i].textContent === "Richard") {
        listItems[i].style.border = "4px dotted";
        break; 
    }
}


document.body.style.fontSize = "36px";


//Bonus:

// Check the background color of the div
var div = document.getElementById("container");
var divBackgroundColor = getComputedStyle(div).backgroundColor;

// Check if the background color is "lightblue"
if (divBackgroundColor === "rgb(173, 216, 230)") {
  // Extract the names from the ul elements
  var ulElements = document.getElementsByClassName("list");
  var users = [];
  for (var i = 0; i < ulElements.length; i++) {
    var liElements = ulElements[i].getElementsByTagName("li");
    for (var j = 0; j < liElements.length; j++) {
      users.push(liElements[j].textContent);
    }
  }

  // Display the alert message
  var message = "Hello " + users[0] + " and " + users[1];
  alert(message);
}