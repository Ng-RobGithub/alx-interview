#!/usr/bin/node

const request = require('request');

// Function to fetch data from the Star Wars API
function fetchStarWarsCharacters(movieId) {
  // Endpoint to fetch film details
  const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

  // Make an HTTP GET request to fetch film details
  request(filmUrl, (error, response, body) => {
    if (error) {
      console.error('Error fetching film details:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Failed to retrieve film details. Status code:', response.statusCode);
      return;
    }

    // Parse the JSON data
    const filmData = JSON.parse(body);

    // Check if the film data is valid
    if (!filmData.characters || filmData.characters.length === 0) {
      console.log('No characters found for this movie.');
      return;
    }

    // Print the movie title
    console.log(`Characters in "${filmData.title}":`);

    // Fetch and print each character
    filmData.characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error fetching character details:', error);
          return;
        }

        if (response.statusCode !== 200) {
          console.error('Failed to retrieve character details. Status code:', response.statusCode);
          return;
        }

        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  });
}

// Get the movie ID from command-line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as a command-line argument.');
  process.exit(1);
}

// Fetch and display characters for the given movie ID
fetchStarWarsCharacters(movieId);
