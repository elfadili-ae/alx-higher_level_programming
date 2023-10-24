#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body);

    const result = {};
    data.forEach(item => {
      if (!(item.userId in result)) {
        result[item.userId] = 0;
      }
      if (item.completed) {
        result[item.userId] += 1;
      }
    });
    console.log(result);
  }
});
