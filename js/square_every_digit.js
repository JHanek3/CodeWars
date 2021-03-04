// Task
// Square every digit, 9119 returns 81181

function squareDigits(num){
  intList = (num.toString()).split('');
  let finStr = ""
  intList.forEach(element => {
    square = Number(element) ** 2
    finStr += square
    // console.log(finStr)
  });
  finStr = Number(finStr);
  return finStr;
  
}

console.log(squareDigits(9119));