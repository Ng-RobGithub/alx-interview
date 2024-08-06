const request = require('request');

const fetchCharacters = async (filmURL) => {
  request(filmURL, async (err, res, body) => {
    if (err) {
      return console.error(err);
    }

    const charURLList = JSON.parse(body).characters;

    for (const charURL of charURLList) {
      await new Promise((resolve, reject) => {
        request(charURL, (err, res, body) => {
          if (err) {
            return console.error(err);
          }
          console.log(JSON.parse(body).name);
          resolve();
        });
      });
    }
  });
};

module.exports = fetchCharacters;
