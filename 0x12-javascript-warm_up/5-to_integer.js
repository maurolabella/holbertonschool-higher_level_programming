#!/usr/bin/node
// write a script that prints "My number: <first argument
//  converted to integer"
const arg = process.argv[2];
if (parseInt(arg, 10)) {
  console.log(`My number: ${parseInt(arg, 10)}`);
} else {
  console.log('Not a number');
}
