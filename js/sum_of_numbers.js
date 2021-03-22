// Task
// Given two integers, which can be positive or negative find the sum of all integers between them and including them

function getSum(a, b) {
  if (a < b) {
    min = a
    max = b
  } else {
    min = b
    max = a
  }
  let range = []
  for (min; min <= max; min++ ) {
    range.push(min)
  }
  
  let sum = 0;
  for (i = 0; i < range.length; i++) {
    sum += range[i]
  }
  return sum;
}

console.log(getSum(1, 0))
console.log(getSum(1, 2))
console.log(getSum(0, 1))
console.log(getSum(1, 1))
console.log(getSum(-1, 0))
console.log(getSum(-1, 2))