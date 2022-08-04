#!/usr/bin/node
// script that concatenates 2 files

const fs = require('fs');

const fileA = fs.readFileSync(`./${process.argv[2]}`, 'utf8');
const fileB = fs.readFileSync(`./${process.argv[3]}`, 'utf8');
const fileConcatenated = fileA + fileB;
fs.writeFile(`${process.argv[4]}`, fileConcatenated, (err) => {
  if (err) {
    console.log(err);
  }
});
