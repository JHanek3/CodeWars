// Task
// complete the solution so that the function will break up camel casing, using a space between words.
// Task
// Insert a space between camel cased letter camelCasing = camel Casing
function solution(string) {
    return string.replace(/[a-z](?=[A-Z])/g, "$& ")
}

console.log(solution("camelCasing"))
console.log(solution("camelCasingTest"))

// complete the function
// function solution(string) {
//     return(string.replace(/([A-Z])/g, ' $1'));
  
//   }