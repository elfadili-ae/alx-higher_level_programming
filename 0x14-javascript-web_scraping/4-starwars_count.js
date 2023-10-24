#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);

  let count = 0;
  const pattern = /people\/18\//;
  for (let i = 0; i < data.count; i++) {
    for (let j = 0; j < data.results[i].characters.length; j++) {
      if (pattern.test(data.results[i].characters[j])) {
        count++;
      }
    }
  }
  console.log(count);
});
