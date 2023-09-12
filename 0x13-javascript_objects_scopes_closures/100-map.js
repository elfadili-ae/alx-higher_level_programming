#!/usr/bin/node

const data = require('./100-data');

console.log(data.list);
const newList = data.list.map((item, index) => {
  return (item * index);
});
console.log(newList);
