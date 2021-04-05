// Task
// Break the ip address down into binary octets
// Then convert the binary to a 32-bit integer

function ipToInt32(ip){
    ipList = ip.split(".")
    ipList.forEach(function(element, index) {
        ipList[index] = parseInt(element).toString(2)
        // console.log(ipList[index].length)
        if (ipList[index].length < 8) {
            ipList[index] = ipList[index].padStart(8, '0')
        }
        
    });

    ipString = ipList.join("")
    start = 31
    fin_num = 0
    
    for (let i = 0; i < ipString.length; i++) {
        if (ipString[i] == "1") {
            fin_num += 2 ** start
            start--;
        } else {
            start--;
        }

    }
    return parseInt(fin_num)
}

console.log(ipToInt32("128.32.10.1"))