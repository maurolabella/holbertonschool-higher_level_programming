#!/usr/bin/node
// function that returns the addition of 2 integers.
// the function must be visible from other files "outside"
function add (x, y) {
  return (Number(x) + Number(y));
}

module.exports = { add };
