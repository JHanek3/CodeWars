// Task
// Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. 

function domainName(url){
  let pattern = /(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]/g
  let firstRegex = String(url.match(pattern))
  // console.log(firstRegex)
  let secondRegex = firstRegex.replace("www.", "")
  // console.log(secondRegex)
  let n = secondRegex.indexOf(".")
  // console.log(n)
  finalRegex = secondRegex.slice(0, n)
  return finalRegex;
}

console.log(domainName("http://google.com"))
console.log(domainName("http://google.co.jp"))
console.log(domainName("https://youtube.com"))
console.log(domainName("www.xakep.ru"))
console.log(domainName("http://github.com/carbonfive/raygun"))
console.log(domainName("http://www.zombie-bites.com"))
console.log(domainName("https://www.cnet.com"))