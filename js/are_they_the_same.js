// Task
// Given two arrays write a function that checks whether the two arrays have the "same" elements
// "Same" means that the elements in b are the elements in a squared, regardless of order

function comp(array1, array2) {
  if (!array1 || !array2 || array1.length !== array2.length) {
    return false;
  }
  else {
    return array1.map(x => x * x).sort().toString() === array2.sort().toString()
  }
}

console.log(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))
console.log(comp([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361]))