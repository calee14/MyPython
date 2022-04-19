let fs = require("fs");
let axios = require("axios");

let songs = []; // song file names
let durations = []; // put duration of songs
let ipfsArray = []; // put ipfs objects here

for (let i = 0; i < songs.length; i++) {
  ipfsArray.push({
    path: `metadata/${i}.json`,
    content: {
      // hash of the post request we made
      // media/0 is the path of the album cover image
      image: `ipfs://Qmc5vRaAsu1yhAucUbFKf29HuR8d7PU1SBsn8FSmBC36ms/media/0`, 
      name: songs[i],
      // get the index of the song file path in the post request we made
      // post request is attained by the hash
      animation_url: `ipfs://Qmc5vRaAsu1yhAucUbFKf29HuR8d7PU1SBsn8FSmBC36ms/media/${}`,
      duration: durations[i],
      artist: "Lil cappin",
      year: "2000"
    },
  });
}

/**
 * This api post req will upload a folder of files to the moralis ipfs
 * These json objects contain the metadata for our minted files 
 */
axios.post("https://deep-index.moralis.io/api/v2/ipfs/uploadFolder", ipfsArray, {
    headers: {
      "X-API-KEY":
        process.env.MORALIS_API_KEY,
      "Content-Type": "application/json",
      accept: "application/json",
    },
  })
  .then((res) => {
    console.log(res.data);
  })
  .catch((error) => {
    console.log(error);
  });