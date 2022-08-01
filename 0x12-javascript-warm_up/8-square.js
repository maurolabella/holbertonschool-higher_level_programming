#!/usr/bin/node
// a script that prints a square

const arg = process.argv[2];
if (Number.isInteger(Number(arg))) {
  const side = Number(arg);
  let row = '';
  for (let i = 0; i < side; i++) {
    row += 'X';
  }
  for (let j = 0; j < side; j++) {
    console.log(row);
  }
} else {
  console.log('Missing size');
}
