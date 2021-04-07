// Task
// magic characters are in the array, have them do battle

function battle(player1, player2) {
    result = {
        'player1': [],
        'player2': []
    }

    length = 0
    if (player1.length == player2.length) {
        length = player1.length 
    } else if (player1.length > player2.length) {
        length = player2.length
    } else {
        length = player1.length
    }

    for (let i = 0; i < length; i++) {
        if (player1[i][0] >= player2[i][1] && player2[i][0] >= player1[i][1]) {
            continue    
        } else if ((player1[i][0] >= player2[i][1] && player2[i][0] < player1[i][1])) {
            result.player1.push(player1[i])
        } else if ((player1[i][0] < player2[i][1] && player2[i][0] >= player1[i][1])) {
            result.player2.push(player2[i])
        } else {
            result.player1.push(player1[i])
            result.player2.push(player2[i])
        }
    }

    if (player1.length > length) {
        for (let i = length; i < player1.length; i++) {
            result.player1.push(player1[i])
        }
    } else {
        for (let i = length; i < player2.length; i++) {
            result.player2.push(player2[i])
        }
    }
    return result
}

// console.log(battle([[1,1]], [[1,1]]))
// console.log(battle([[1,2]], [[1,1]]))
// console.log(battle([[1,2]], [[1,2]]))
// console.log(battle([[1, 1], [2, 1], [2, 2], [5, 5]], [[1, 2], [1, 2], [3, 3]]))
// console.log(battle([[1, 1], [2, 1], [2, 2], [5, 5]], [[1, 2], [1, 2], [3, 3]]))
console.log(battle([ [ 8, 2 ], [ 9, 4 ], [ 1, 6 ], [ 2, 4 ], [ 4, 8 ] ], [ [ 8, 3 ], [ 6, 9 ], [ 6, 4 ] ]))

// LOL
const battle = (player1, player2) => {
    return {
      player1: player1.filter((c, i) => !player2[i] || c[1] > player2[i][0]),
      player2: player2.filter((c, i) => !player1[i] || c[1] > player1[i][0]),
    }
  }

//LOL