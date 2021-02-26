// Task
// Make a function that can take any non-negative int as an arguemnt and return it with its digits in descending order
function descendingOrder(n){
  n = Number((((n.toString().split("")).sort()).reverse()).join(""))
  return n
}

console.log(descendingOrder(42145))