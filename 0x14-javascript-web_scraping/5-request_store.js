#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(process.argv[3], body, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    }
  });
});
