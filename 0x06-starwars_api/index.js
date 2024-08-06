#!/usr/bin/node
const fetchCharacters = require('./fetchCharacters');

const filmNum = process.argv[2];
const filmURL = `https://swapi-api.hbtn.io/api/films/${filmNum}/`;

fetchCharacters(filmURL);
