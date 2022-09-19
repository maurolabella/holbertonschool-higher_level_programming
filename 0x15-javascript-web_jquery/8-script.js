// Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', data => {
  data.results.forEach(mov => {
    $('#list_movies').append(`<li>${mov.title}</li>`);
  });
});
