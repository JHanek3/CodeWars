// Task
// The second and last characters are switched
// the first letter is replaced with its character code

function decipherThis(str) {
    splited = str.split(" ");
    fin_array = []
    for (let i = 0; i < splited.length; i++) {
        let numberPattern = /\d+/g;
        first_letter = String.fromCharCode(parseInt(splited[i].match(numberPattern)));
        switch_str = splited[i].replace(numberPattern, "")
        

        if (i == 0) {
            first_letter.toUpperCase();
        }

        if (switch_str.length == 0) {
            fin_str = first_letter;
        } else if (switch_str.length == 1) {
            fin_str = first_letter + switch_str;
        } else {
            fin_str = first_letter + switch_str.substring([switch_str.length - 1], switch_str.length) + switch_str.substring(1, switch_str.length - 1) + switch_str.substring(0, 1);
        }
        fin_array.push(fin_str)
    }
    return fin_array.join(" ");
}; 

console.log(decipherThis("72olle 103doo 100ya"));
console.log(decipherThis('82yade 115te 103o'))
console.log(decipherThis('72eva 97 103o 97t 116sih 97dn 115ee 104wo 121uo 100o'))