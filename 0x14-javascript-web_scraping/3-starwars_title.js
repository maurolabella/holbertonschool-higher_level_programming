#!/usr/bin/node
// Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

const axios = require('axios').default;

axios.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`)
  .then((response) => console.log(response.data.title))
  .catch((error) => console.log(error.response.status));
