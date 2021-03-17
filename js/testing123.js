var number=function(array){
  for (i = 0; i < array.length; i++) {
    array[i] = `${i + 1}: ${array[i]}`
  }
  return (array)
}

console.log(number([]))
console.log(number(["a", "b", "c"]))