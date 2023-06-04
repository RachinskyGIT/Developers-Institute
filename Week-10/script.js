// const largeNumber = require('./main');
// const b = 5;
// const sum = largeNumber + b;
// console.log('Sum:', sum);


// const http = require('http');
// const server = http.createServer((req, res) => {
//     res.setHeader('Content-Type', 'text/html');
//     res.statusCode = 200;
  
//     const largeNumber = require('./main');
//     const result = `<p>My Module is ${largeNumber}</p>`;
//     const message = '<h1>Hi there at the frontend</h1>';
  
//     res.end(result + message);
//   });
  
//   server.listen(3000, () => {
//     console.log("I'm listening");
//   });

  
const http = require('http');
const getCurrentDateTime = require('./main');

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/html');
  res.statusCode = 200;

  const dateTime = getCurrentDateTime();
  const responseHTML = `<p>Current date and time: ${dateTime}</p>`;

  res.end(responseHTML);
});

server.listen(8080, () => {
  console.log("Server is running at http://localhost:8080/");
});
