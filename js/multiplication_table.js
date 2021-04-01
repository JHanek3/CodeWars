// Task
// Return a multiplication table

function multiplicationTable(row,col){
    master_array = []
    push_array = []
    while (master_array.length < row) {
        for (let x = 1; x <= row; x++) {
            for (let y = 1; y <= col; y++) {
                push_array.push(x * y)
                if (y == col) {
                    master_array.push(push_array)
                    push_array = []
                }
            }
        }  
    }

    return master_array  
}

console.log(multiplicationTable(2,2))
console.log(multiplicationTable(3,3))
console.log(multiplicationTable(2,5))