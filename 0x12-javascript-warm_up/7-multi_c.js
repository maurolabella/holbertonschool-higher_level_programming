#!/usr/bin/node
// script that prints x times "C is fun"
const arg = process.argv[2];
if (Number.isInteger(Number(arg))) {
  for (let i = 0; i < Number(arg); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
