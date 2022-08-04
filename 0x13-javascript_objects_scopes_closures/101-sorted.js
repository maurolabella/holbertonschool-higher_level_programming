#!/usr/bin/node
// Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
const { dict } = require('./101-data');

const newDict = Object.entries(dict).reduce((user, index) => {
  !user[index[1]]
    ? user[index[1]] = [index[0]]
    : user[index[1]].push(index[0]);
  return user;
}, {});
console.log(newDict);
