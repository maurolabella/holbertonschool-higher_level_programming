#!/usr/bin/node
// write a class Rectangle that defines a rectangle

class Rectangle {
  // class methods
  constructor (w, h) {
    // constructor takes width and height
    if ([isNaN(w), isNaN(h), w <= 0, h <= 0].some((currentValue) => currentValue === true)) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let i = 0;
    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }
}

module.exports = Rectangle;
