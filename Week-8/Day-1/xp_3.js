// Declare a global variable named allBoldItems.
let allBoldItems = document.querySelectorAll('strong');

// Create a function called getBoldItems() that takes no parameter. 
// This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.
function getBoldItems() {
    allBoldItems = document.querySelectorAll('p strong');
  }

var paragraph = document.querySelector('p');

// Function to be called on mouseover (highlight)
function highlight() {
    allBoldItems.forEach(function(item) {
      item.style.color = 'blue';
    });
}
  
// Function to be called on mouseout (return to default)
function returnItemsToDefault() {
    allBoldItems.forEach(function(item) {
      item.style.color = 'white';
    });
}
  
// Add event listener for mouseover
paragraph.addEventListener('mouseover', highlight);
  
// Add event listener for mouseout
paragraph.addEventListener('mouseout', returnItemsToDefault);
  