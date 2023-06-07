// xp2_1
const express = require('express');
const app = express();
const port = 3000;
const user = { firstname: 'John', lastname: 'Doe' };

app.get('/users', (req, res) => {
  res.send(JSON.stringify(user));
});

app.get('/:id', (req, res) => {
    const id = req.params.id;
    res.send(`ID: ${id}`);
    console.log({ id });
  });
  
app.use(express.static('public_folder'));




app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
    console.log(user);
});
