#!/usr/bin/node
// visible function that takes input, increments it by 1
// and use the result as a parameter for a function that
// is also given

function addMeMaybe (n, func) {
  func(n + 1);
}
module.exports = { addMeMaybe };
