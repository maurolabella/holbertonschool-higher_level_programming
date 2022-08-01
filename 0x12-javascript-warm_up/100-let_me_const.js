#!/usr/bin/node
// modify myvar through exporting a file

myVar = 333;
module.exports.module = myVar;
