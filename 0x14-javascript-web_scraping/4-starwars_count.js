#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body).results;
    const dataString = JSON.stringify(data);

    const pattern = /people\/18\//g;
    const matches = dataString.match(pattern);

    if (matches) {
      console.log(matches.length);
    } else {
      console.log(0);
    }
  }
});
