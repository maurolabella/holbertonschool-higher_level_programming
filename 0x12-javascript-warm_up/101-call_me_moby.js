#!/usr/bin/node
// executes x times a function (visible function)

function callMeMoby (num, func) {
  for (let i = 0; i < num; i++) {
    func();
  }
}
module.exports = { callMeMoby };
