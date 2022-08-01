#!/usr/bin/node
// script that prints the addition of 2 integers

const sum1 = process.argv[2];
const sum2 = process.argv[3];
function add (a, b) {
  return (a + b);
}
if (isNaN(sum1) || isNaN(sum2)) {
  console.log('NaN');
} else {
  console.log(`${add(Number(sum1), Number(sum2))}`);
}
