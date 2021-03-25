/*
Task
A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of 3, 4, 5 or more characters. 
The 1st character of a code is a capital letter which defines the book category. (e.g. : M)

In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) which indicates the quantity of books of this code in stock.

You will be given a stocklist (e.g. : L) and a list of categories in capital letters e.g :
and your task is to find all the books of L with codes belonging to each category of M and to sum their quantity according to each category.

*/

function stockList(listOfArt, listOfCat){
  if (listOfArt.length == 0 || listOfCat.length == 0) {
    return ""
  }

  let result = {}
  let r = /\d+/;
  
  for (var i = 0; i < listOfArt.length; i++) {
    // console.log(r.exec(listOfArt[i])[0]);
    let value = Number(r.exec(listOfArt[i])[0])
    
    // console.log(listOfArt[i][0])
    // console.log(value)
    
    if (listOfArt[i][0] in result) {
      let addValue = result[listOfArt[i][0]]
      // console.log(addValue)
      result[listOfArt[i][0]] = value + addValue
    } else {
      result[listOfArt[i][0]] = value;
    }
  }
  // console.log(result)

  
  let result2 = {}
  for (var i = 0; i < listOfCat.length; i++) {
    result2[listOfCat[i]] = 0
    for (const [key, value] of Object.entries(result)) {
      if (listOfCat[i] == key) {
        result2[listOfCat[i]] = value 
      }
    }
  }

  // console.log(result2)

  fin_string = ""
  let iterator = 0;
  for (const [key, value] of Object.entries(result2)) {
    if (iterator == 0) {
      fin_string = `(${key} : ${value})`
      iterator ++;
    } else {
      fin_string += ` - (${key} : ${value})`
    }
  }
  return fin_string
}


console.log(stockList(["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B"]))
console.log(stockList(["CBART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"], ["A", "B", "C", "W"]))