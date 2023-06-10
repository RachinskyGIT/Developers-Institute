// import the Express module and create an instance of the Express application.
const express = require('express');
const app = express();

// Set up the route /aboutMe/:hobby using the app.get() method. Check if the hobby parameter is a string, 
// and send the hobby as the response. If the parameter is not a string, set the status to 404.
app.get('/aboutMe/:hobby', (req, res) => {
    const hobby = req.params.hobby;
  
    if (typeof hobby === 'string') {
      res.send(hobby);
    } else {
      res.status(404).send('Invalid hobby');
    }
  });

// Set up the route /pic to serve the HTML file containing a picture. Use the express.static middleware to serve static files from the public folder.  
app.use(express.static('public'));

// Set up the route /formData to handle the form submission. Use the app.post() method to handle the form submission data. 
// Retrieve the email and message from the request body and send them as the response.
app.post('/formData', (req, res) => {
    // const email = req.body.email;
    // const message = req.body.message;
    const { email, message } = req.query;
    res.send(`${email} sent you a message: "${message}"`);
  });
  

// Start the server and listen on the desired port (e.g., 3000).
app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
  });
  

