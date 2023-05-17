// ex5

// Retrieve the <li> elements within the first <ul> with class "list"
var listItems = document.querySelectorAll("ul.list:nth-of-type(1) li");

// Iterate over the <li> elements to find and remove the one containing "Sarah"
for (var i = 0; i < listItems.length; i++) {
    if (listItems[i].textContent === "Pete") {
        listItems[i].textContent = "Richard";
        break; 
    }
}
// Log the updated HTML content
var containerDiv = document.getElementById("container");
console.log(containerDiv.innerHTML);




// Retrieve the <li> elements within the second <ul> with class "list"
var listItems = document.querySelectorAll("ul.list:nth-of-type(2) li");

// Iterate over the <li> elements to find and remove the one containing "Sarah"
for (var i = 0; i < listItems.length; i++) {
    if (listItems[i].textContent === "Sarah") {
        listItems[i].parentNode.removeChild(listItems[i]);
        break; 
    }
}

// Log the updated HTML content
var containerDiv = document.getElementById("container");
console.log(containerDiv.innerHTML);




// Add the class "student_list" to both <ul> elements
var ulElements = document.querySelectorAll("ul.list");
ulElements.forEach(function(ul) {
    ul.classList.add("student_list");
});

// Add the classes "university" and "attendance" to the first <ul>
var firstUl = document.querySelector("ul.list:first-of-type");
firstUl.classList.add("university", "attendance");

// Log the updated HTML content
var containerDiv = document.getElementById("container");
console.log(containerDiv.innerHTML);
