#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = JSON.parse(body).characters;

  printItem(characters, 0);
});

function printItem (item, index) {
  request(item[index], (err, resp, bdy) => {
    if (err) {
      console.error(err);
      return;
    }
    const dt = JSON.parse(bdy);
    console.log(dt.name);
  });
  if (index + 1 < item.length) {
    printItem(item, index + 1);
  }
}
