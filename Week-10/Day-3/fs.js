const fs = require('fs');

fs.writeFile('output.txt', 'Some Text To See', 'utf8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('File created and written to successfully!');
  });

fs.appendFile('output.txt', 'Buy orange juice', 'utf8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('Text appended to the file successfully!');
  });
  
fs.unlink('output.txt', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('File deleted successfully!');
  });
  