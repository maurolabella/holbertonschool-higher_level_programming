#!/usr/bin/node
// script that prints the factorial of first argument

const number = process.argv[2];

function factorial (a) {
  if (a <= 1) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}
if (isNaN(number)) {
  console.log(1);
} else {
  console.log(`${factorial(Number(number))}`);
}
