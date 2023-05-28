const form = document.getElementById('myForm');
const output = document.getElementById('output');

form.addEventListener('submit', function(event) {
  event.preventDefault();

  // Get input values
  const name = document.getElementById('name').value;
  const surname = document.getElementById('surname').value;

  // Create JSON object
  const data = {
    name: name,
    surname: surname
  };

  // Convert JSON object to string
  const json = JSON.stringify(data);

  // Append JSON string to the DOM
  output.textContent = json;
});