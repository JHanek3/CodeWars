// Task
// Create a function called encode() that replaces all lowercase vowels in a given string

function encode(string) {
    res = string.replace(/a/g, "1");
    res = res.replace(/e/g, "2");
    res = res.replace(/i/g, "3");
    res = res.replace(/o/g, "4");
    res = res.replace(/u/g, "5");
    return res
  }
  
  function decode(string) {
    res = string.replace(/1/g, "a");
    res = res.replace(/2/g, "e");
    res = res.replace(/3/g, "i");
    res = res.replace(/4/g, "o");
    res = res.replace(/5/g, "u");
    return res
  }

console.log(encode('hello'))
console.log(encode('How are you today?'))
console.log(encode('This is an encoding test.'))
console.log(decode('h2ll4' ))

// const encode = s => s.replace(/[aeiou]/g, v => ' aeiou'.indexOf(v));
// const decode = s => s.replace(/\d/g, v => ' aeiou'[v]);