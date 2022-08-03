#!/usr/bin/node
// write a function that returns the reversed version of a list

exports.esrever = function (list) {
  return list.reduce((reverted, current) => {
    reverted.unshift(current);
    return reverted;
  }, []);
};
