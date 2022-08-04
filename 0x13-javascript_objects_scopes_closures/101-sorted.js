#!/usr/bin/node
// Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
const { dict } = require('./101-data');

const newDict = Object.entries(dict).reduce((index, data) => {
  !index[data[1]]
    ? index[data[1]] = [data[0]]
    : index[data[1]].push(data[0]);
  return index;
}, {});
console.log(newDict);
