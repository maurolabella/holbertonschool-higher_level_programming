// Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', data => {
  $('#character').append(`<p>${data.name}</p>`);
});
