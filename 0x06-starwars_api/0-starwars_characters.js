#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie
 * The first positional argument passed is the Movie ID
 * Display one character name per line in the same order
 * as the list in the /films/ endpoint
 */

const axios = require('axios');
const filmNum = process.argv[2];
const filmURL = `https://swapi-api.hbtn.io/api/films/${filmNum}/`;

const getCharacterNames = async (filmURL) => {
  try {
    // Fetch the film data
    const filmResponse = await axios.get(filmURL);
    const charURLs = filmResponse.data.characters;

    // Fetch and print each character's name
    for (const charURL of charURLs) {
      const charResponse = await axios.get(charURL);
      console.log(charResponse.data.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
};

getCharacterNames(filmURL);
