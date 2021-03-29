// Task
// Replaces a letteer with the letter 13 letters after it in the alphabet

ceaser = {"a": "n","A": "N","b": "o","B": "O","c": "p","C": "P","d": "q","D": "Q","e": "r","E": "R","f": "s","F": "S","g": "t","G": "T","h": "u","H": "U","i": "v","I": "V","j": 
"w","J": "W","k": "x","K": "X","l": "y","L": "Y","m": "z","M": "Z","n": "a","N": "A","o": "b","O": "B","p": "c","P": "C","q": "d","Q": "D","r": "e","R": "E","s": "f","S": "F",
"t": "g","T": "G","u": "h","U": "H","v": "i","V": "I","w": "j","W": "J","x": "k","X": "K","y": "l","Y": "L","z": "m","Z": "M"}

function rot13(message){
    ceaser_str = ""
    for (let i = 0; i < message.length; i++) {
        if (/\d/.test(message[i]) || /[\s~.`!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/g.test(message[i])) {
            ceaser_str += message[i]
        }
        for (const [key, value] of Object.entries(ceaser)) {
            if (message[i] == key) {
                ceaser_str += value
            }
        }
    }
    return ceaser_str
}
console.log(rot13("test1"))
console.log(rot13("Test"))
console.log(rot13("10+2 is twelve."))

// function rot13(message) {
//     var a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
//     var b = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
//     return message.replace(/[a-z]/gi, c => b[a.indexOf(c)])
//   }