// Task
// Your task is to pslit the choclate bar of a given dimension n * m into smaller squares, implement a function that will return minimum number of breaks needed
// 2 * 1 = 1
// 3 * 1 = 2
// 5 * 5 = 24
// 1 * 1 || invalid = 0

function breakChocolate(n,m) {
  if (n * m <= 1) {
   return 0; 
  }
  else {
    return n * m - 1;
  }
  
}