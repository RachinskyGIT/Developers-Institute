fetch('/users')
  .then(response => response.json())
  .then(data => {
    console.log(data); // Output the JSON object in the console
    // Display the JSON object on the DOM or perform any other actions
  })
  .catch(error => console.log(error));
