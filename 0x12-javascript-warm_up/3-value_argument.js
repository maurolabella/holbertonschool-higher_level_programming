#!/usr/bin/node
// Write a script that prints the first argument passed to it
const args = process.argv[2];
if (args) {
  console.log(args);
} else {
  console.log('No argument');
}
