#!/usr/bin/node
// imports an array and computes a new array using map.

const { list } = require('./100-data.js');
console.log(list);
console.log(list.map((current, index) => current * index));
