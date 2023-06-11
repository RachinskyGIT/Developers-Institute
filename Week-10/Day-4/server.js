const registerForm = document.querySelector('#register-form');
const loginForm = document.querySelector('#login-form');
const registerButton = document.querySelector('#register-button');
const loginButton = document.querySelector('#login-button');

registerForm.addEventListener('input', () => {
  const inputs = registerForm.querySelectorAll('input');
  const isEmpty = Array.from(inputs).some(input => input.value === '');
  registerButton.disabled = isEmpty;
});

loginForm.addEventListener('input', () => {
  const inputs = loginForm.querySelectorAll('input');
  const isEmpty = Array.from(inputs).some(input => input.value === '');
  loginButton.disabled = isEmpty;
});


const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse request body
app.use(express.json());

// Register route
app.post('/register', (req, res) => {
  // Retrieve the data from req.body (e.g., req.body.firstName, req.body.lastName, etc.)
  // Use Knex or any other database library to store the data in the database
  // Return a response or send a success message
});

// Login route
app.post('/login', (req, res) => {
  // Retrieve the data from req.body (e.g., req.body.username, req.body.password)
  // Use Knex or any other database library to validate the credentials
  // Return a response or send a success message
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
