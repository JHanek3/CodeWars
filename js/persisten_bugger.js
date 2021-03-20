// Task
// Write a function, persistence, that takes in a positive parameter and returns its
// multiplicate persistence, which is the umber of times you multiply its digits until
// you reach a single digit

function persistence(num) {
  let sum = 0;

  function theSplitter(arr) {
    let value = 1
    splitArr = String(arr).split("").map(Number)
      for (let i = 0; i < splitArr.length; i++) {
      value *= splitArr[i]
    }
    sum += 1
    return value
  }

  if (num < 9) {
    return sum
  } else {
      var firstSplit = theSplitter(num)
      if (firstSplit <= 9) {
        return sum
      } else {
        value = firstSplit
        while (value > 9) {
          value = theSplitter(value)
        }
        return sum
      }
  }
}

console.log(persistence(39))
console.log(persistence(999))
console.log(persistence(4))
console.log(persistence(25))
console.log(persistence(91))