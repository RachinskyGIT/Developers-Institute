// xp1_2
const http = require('http');

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'application/json');
  res.statusCode = 200;

  const user = {
    firstname: 'John',
    lastname: 'Doe'
  };

  res.end(JSON.stringify(user));
});

server.listen(8080, () => {
  console.log('Server is running at http://localhost:8080/');
});
