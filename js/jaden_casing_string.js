// Capitalize the first letter in every word

String.prototype.toJadenCase = function () {
  // you need this.split not str.split
  capList = this.split(" ");
  finList = []
  capList.forEach(word => 
    // console.log(word),
    // console.log(word.charAt(0).toUpperCase() + word.slice(1)),
    finList.push(word.charAt(0).toUpperCase() + word.slice(1))
  )
  finStr = finList.join(" ");
  return finStr
};

var str = "How can mirrors be real if our eyes aren't real";
console.log(str.toJadenCase())
console.log(str.toJadenCase() == "How Can Mirrors Be Real If Our Eyes Aren't Real");