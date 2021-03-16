// Task, format a string as follows Bart. Bart & Lisa, Bart, Lisa,& Maggie

function list(names){
  if (names.length == 0) {
    return '';
  } else {
    fin_array = []
    names.forEach(name => {
      fin_array.push(name.name)
    })
    // console.log(fin_array)
    if (fin_array.length == 1) {
      return fin_array.toString()
    } 
    else if (fin_array.length == 2) {
      return `${fin_array[0]} & ${fin_array[1]}`
    } else {
      fin_string = '';
      for (var i = 0; i < fin_array.length; i++) {
        if (i == fin_array.length - 1) {
          fin_string += `& ${fin_array[i]}`
        } else if (i == fin_array.length - 2) {
          fin_string += `${fin_array[i]} `
        } else {
          fin_string += `${fin_array[i]}, `
        }
      }
      return fin_string;
    }
  }
}

console.log(list([]));
console.log(list([{name: 'Bart'}]));
console.log(list([{name: 'Bart'}, {name: 'Lisa'}]));
console.log(list([{name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'}]));
console.log(list([{name: 'Bart'},{name: 'Lisa'},{name: 'Maggie'},{name: 'Homer'},{name: 'Marge'}]))