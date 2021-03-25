// Task
// A stream of data is received and needs to be reversed.
// Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

function dataReverse(data) {
    let result = []
    let arrayCopy = [...data]
    while (arrayCopy.length > 0) {
        result.push(arrayCopy.splice(0, 8))
    }
    reversedResult = result.reverse()
    //flat(), dont work lame
    // return reversedResult.flat()
    return reversedResult.reduce((acc, val) => acc.concat(val), []);
}

console.log(dataReverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]))