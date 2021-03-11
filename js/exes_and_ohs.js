// Check to see if the string has the same amount of x's and o's

function XO(str) {
  return ((str.toLowerCase().match(/x/g) || []).length) == ((str.toLowerCase().match(/o/g) || []).length);
}

console.log(XO("ooxx"));
console.log(XO("xxOo"));
console.log(XO("xooxx"));
console.log(XO("zpzpzpp"));