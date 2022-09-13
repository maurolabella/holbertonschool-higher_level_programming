#!/usr/bin/node
/* Write a script that prints the number of movies where the character “Wedge Antilles” is present. */

const axios = require('axios').default;

axios.get(`${process.argv[2]}`)
  .then((response) => {
    let count = 0;
    for (let idA = 0; idA < response.data.results.length; idA++) {
      for (let idB = 0; idB < response.data.results[idA].characters.length; idB++) {
        if (response.data.results[idA].characters[idB].includes('18')) {
          count += 1;
        }
      }
    }
    console.log(count);
  })
  .catch((error) => console.log(error));
