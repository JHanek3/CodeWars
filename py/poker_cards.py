# Task
# Encode and decode poker cards
# encoded ['Ac', 'Ks', '5h', 'Td', '3c'] -> [0, 2 ,22, 30, 51] 
# decoded [0, 51, 30, 22, 2] -> ['Ac', '3c', 'Td', '5h', 'Ks']

my_dic = {0:'Ac', 1:'2c', 2:'3c', 3:'4c', 4:'5c', 5:'6c', 6:'7c', 7:'8c', 8:'9c', 9:'Tc', 10:'Jc', 11:'Qc', 12:'Kc', 13:'Ad', 14:'2d',
    15:'3d', 16:'4d', 17:'5d', 18:'6d', 19:'7d', 20:'8d', 21:'9d', 22:'Td', 23:'Jd', 24:'Qd', 25:'Kd', 26:'Ah', 27:'2h', 28:'3h', 29:'4h', 
    30:'5h', 31:'6h', 32:'7h', 33:'8h', 34:'9h', 35:'Th', 36:'Jh', 37:'Qh', 38:'Kh', 39:'As', 40:'2s', 41:'3s', 42:'4s', 43:'5s', 44:'6s', 
    45:'7s', 46:'8s', 47:'9s', 48:'Ts', 49:'Js', 50:'Qs', 51:'Ks',
}

def encode(cards):
    fin_array = []
    for x in range(len(cards)):
        for (key, value) in my_dic.items():
            if value == cards[x]:
                fin_array.append(key)
    fin_array.sort()
    return fin_array

def decode(cards):
    fin_array = []
    cards.sort()
    for x in range(len(cards)):
        for (key, value) in my_dic.items():
            if key == cards[x]:
                fin_array.append(value)
    return fin_array

print(encode(["Td", "8c", "Ks"]))
print(encode(['Ac', 'Ks', '5h', 'Td', '3c']))
print(decode([0, 51, 30, 22, 2]))
print(decode([7, 22, 51]))

# Interesting
# str = "A23456789TJQK"
# card = "cdhs"

# def encode(cards):
#     return sorted([card.index(x[1]) * 13 + str.index(x[0]) for x in cards])

# def decode(cards):
#     return [f"{str[x % 13]}{card[x // 13]}" for x in sorted(cards)]