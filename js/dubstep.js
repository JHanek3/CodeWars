// Task
// Given a string with WUBAWUBB return A B
// Basically remove the WUB to make a song

function songDecoder(song){
  let regexWUB = /WUB/g;
  song = song.replace(regexWUB, " ");
  song = song.replace( /\s\s+/g, ' ' )
  song = song.trim();
  return song;
}

console.log(songDecoder("AWUBBWUBC"))
console.log(songDecoder("AWUBWUBWUBBWUBWUBWUBC", " "));
console.log(songDecoder("WUBAWUBBWUBCWUB", " "));
console.log(songDecoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"));