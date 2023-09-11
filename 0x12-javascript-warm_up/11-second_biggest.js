#!/usr/bin/node

const argv = process.argv;
let max = 0;
let max_2 = 0;

if (argv.length > 3) {
  for (let i = 2; i < argv.length; i++) {
    const num = parseInt(argv[i]);
    if (num > max) {
      max = num;
    }
  }
  for (let i = 2; i < argv.length; i++) {
    const num = parseInt(argv[i]);
    if (num != max && num > max_2) {
      max_2 = num;
    }
  }
}
console.log(max_2);
