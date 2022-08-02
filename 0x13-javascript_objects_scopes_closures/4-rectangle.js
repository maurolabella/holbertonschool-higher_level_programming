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

  // create an instance method to print
  print () {
    let i = 0;
    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }

  // create an instance method to rotate
  rotate () {
    this.width = this.width + this.height;
    this.height = this.width - this.height;
    this.width = this.width - this.height;
  }

  // create an instance method to double
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
