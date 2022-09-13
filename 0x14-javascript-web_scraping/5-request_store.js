#!/usr/bin/node
/*
Write a script that gets the contents of a webpage and stores it in a file.

The first argument is the URL to request
The second argument the file path to store the body response
The file must be UTF-8 encoded
You must use the module axios
*/

const axios = require('axios').default;
const fs = require('fs');

axios.get(`${process.argv[2]}`)
  .then((response) => fs.writeFile(process.argv[3], response.data, 'utf-8', (err) => { if (err) { console.log(err); } }))
  .catch((error) => console.log(error.response.status));
