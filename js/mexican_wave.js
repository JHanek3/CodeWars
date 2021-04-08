// Task
// Create a function that does the wave through each word
// "hello" -> Hello hEllo HeLlo helLo hellO

function wave(str){
    let finArray = []
    for (let i = 0; i < str.length; i++) {
        if (str[i] == " ") {
            continue
        } else 
            // console.log(str[i].toUpperCase())
            // console.log(str.substring(i + 1, str.length))
            // console.log(str.substring(0, i + 1))
            finArray.push(str.substring(0, i) + str[i].toUpperCase() + str.substring(i + 1, str.length))
    }
    return finArray
}

console.log(wave("hello"))
console.log(wave("Two words"))