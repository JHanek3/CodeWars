// Task
// Vasya is currently working as a clerk, he wants to sell a ticket to every person in line
// Can vasya sell a ticket to every person and given change if he initially has no money and sells the tickets in the order q (array)

function tickets(peopleInLine){

  registerArray = [];
  can = "YES"
  
  peopleInLine.forEach((element) => {
    if (element == 25) {
      registerArray.push(element);
    } 
    
    else if (element == 50) {
      if (registerArray.includes(25)) {
        console.log(registerArray)
        registerArray.pop(25);
        registerArray.push(50);
        console.log(registerArray)
      } else {
        can = "NO";

      }
    }
  })
}

console.log(tickets([25, 25, 50, 50]))
// console.log(tickets([25,100]))
// console.log(tickets([25,25,50,100,25,50,25,100,25,25,50,100,25,50,50,100]))