#!/usr/bin/node
// detect the number of arguments already printed and the new
// argument value

exports.logMe = (function (item) {
  let arg = 0;
  return function (item) {
    // output format:
    console.log(`${arg}: ${item}`);
    arg += 1;
  };
}());
