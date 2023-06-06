const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('<p>Hello, this is an HTML line of code!</p>');
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}/`);
});
