# Task
# ! are 2, ? are 3 given two strings who costs more?
from collections import Counter

def balance(left, right):
    c = dict(Counter(left))
    d = dict(Counter(right))
    leftTotal = 0
    rightTotal = 0

    for key, value in c.items():
        if key == "!":
            leftTotal += value * 2
        if key == "?":
            leftTotal += value * 3
    for key, value in d.items():
        if key == "!":
            rightTotal += value * 2
        if key == "?":
            rightTotal += value * 3
    
    if leftTotal > rightTotal:
        return "Left"
    elif leftTotal < rightTotal:
        return "Right"
    else:
        return "Balance"

print(balance("",""))
print(balance("!!","??"))
print(balance("!??","?!!"))
print(balance("!?!!","?!?"))
print(balance("!!???!????","??!!?!!!!!!!"))