#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
};
