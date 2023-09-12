#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');

fs.readFile(argv[2], 'utf8', (err, data1) => {
  if (err) {
    console.log('Error reading the file ' + argv[2]);
  }
  const txt1 = data1;

  fs.readFile(argv[3], 'utf8', (err, data2) => {
    if (err) {
      console.log('Error reading the file ' + argv[3]);
    }
    const txt2 = data2;

    const combo = txt1 + '\n' + txt2;
    fs.writeFile(argv[4], combo, 'utf8', (err) => {
      if (err) {
        console.log('Error writing to the file ' + argv[4]);
      }
    });
  });
});
