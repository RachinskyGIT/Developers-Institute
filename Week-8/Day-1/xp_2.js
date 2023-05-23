// Retrieve the form and console.log it.
var formText = document.querySelector("form").textContent;
console.log(formText)


// Retrieve the form and inputs
const form = document.querySelector('form');
var usersAnswerList = document.querySelector('.usersAnswer');
const firstNameInput = document.getElementById('fname');
const lastNameInput = document.getElementById('lname');
  // Listen for form submission
  form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the refresh page and delete console output after form submission

    if (firstNameInput && lastNameInput) {  // Check if the input values are not empty
    // Log the input values
    console.log(firstNameInput.value);
    console.log(lastNameInput.value);

    // Create <li> elements for the input values
    var firstNameItem = document.createElement('li');
    var lastNameItem = document.createElement('li');

    // Set the text content of the <li> elements
    firstNameItem.textContent = firstNameInput.value;
    lastNameItem.textContent = lastNameInput.value;

    // Append the <li> elements to the <ul> element
    usersAnswerList.appendChild(firstNameItem);
    usersAnswerList.appendChild(lastNameItem);

    }
  });


// Retrieve the inputs by their name attribute and console.log them.
form.addEventListener('submit', function(event) {
event.preventDefault(); // Prevent the refresh page and delete console output after form submission
// Log the input values
console.log(firstElement.value);
console.log(secondElement.value);
});


