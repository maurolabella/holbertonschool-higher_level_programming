#!/usr/bin/node
/* Write a script that computes the number of tasks completed by user id. */

const axios = require('axios').default;

axios.get(`${process.argv[2]}`)
  .then((response) => {
    const res = response.data;
    console.log(res.reduce((obj, el) => {
      if (el.completed) {
        obj[el.userId]
          ? obj[el.userId]++
          : obj[el.userId] = 1;
      }
      return obj;
    }, {}));
  })
  .catch((error) => console.log(error));
