#!/usr/bin/node
// write a class Square that extends and inherits from Rectangle
// of 4-rectangle.js

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  // I must use class notation and extends
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
