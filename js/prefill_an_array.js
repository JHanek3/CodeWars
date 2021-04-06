// Task
// create the function prefill that returns an array of n elements that all have the same value v, do this without a for loop
function prefill(n, v) {
  
    const arr = []
    
    if (typeof n === "boolean" || !isFinite(n) || !Number.isInteger(Number(n)) || Number(n) < 0) {
        throw new TypeError(`${n} is invalid`)
    }

            
    while (arr.length < parseInt(n)) {
        arr.push(v)
    }
    return arr
}

console.log(prefill('2.8244740028055197',1))
console.log(prefill("infinity" ,1))
// console.log(prefill(2, 'abc'))
// console.log(prefill("1", 1))
// console.log(prefill(3, prefill(2,'2d')))
// console.log(prefill("xyz", 1))
// console.log(prefill(false, 1))