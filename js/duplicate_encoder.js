// Task
// Convert a string to a new string where each character in the new string follows
//1 occurance == (
//else == )

function duplicateEncode(word){
  lowerWord = word.toLowerCase()
  result = {}
  for (var i = 0; i < lowerWord.length; i++) {
    if(!result[lowerWord[i]]) {
      result[lowerWord[i]] = 0;
    }
    result[lowerWord[i]]++;  
  }
  // console.log(result)

  fin_string = ""
  for (var i=0; i < lowerWord.length; i++) {
    // console.log(word[i])
    for (const [key, value] of Object.entries(result)) {
      if (key == lowerWord[i]) {
        if (value == 1) {
          fin_string += "("
        } else {
          fin_string += ")"
        }
      }
    }
  }
  return fin_string
}

console.log(duplicateEncode("din"))
console.log(duplicateEncode("recede"))
console.log(duplicateEncode("Success"))
console.log(duplicateEncode("(( @" ))