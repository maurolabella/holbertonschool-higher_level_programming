#!/usr/bin/node
// write a function that returns the number of occurrencess in a list

function nbOccurences (list, searchValue) {
  return list.reduce((count, current) => {
    if (current === searchValue) {
      count++;
    }
    return count;
  }, 0);
}

module.exports = { nbOccurences };
