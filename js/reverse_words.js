// receive a string and reverse each word in the string but keep the order
// this space -> siht ecaps

function reverseWords(str) {
  fin_array = []
  str = (((str.split('')).reverse()).join("")).split(" ")

  str.forEach(word => fin_array.push(word))
  fin_array.reverse()
  
  return fin_array.join(" ")
}

console.log(reverseWords("This is an example!"))
console.log(reverseWords("double  spaces"))