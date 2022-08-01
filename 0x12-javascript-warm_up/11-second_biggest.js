#!/usr/bin/node
// a script that searches the second biggest integer in the list of arguments

const a = process.argv.length;

if (a <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  args.sort(function (a, b) { return b - a; });
  console.log(args[1]);
}
