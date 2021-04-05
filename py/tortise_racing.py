# Task
# Two tortises are racing
# v1 = velocity of turtle1
# v2 = velocity of turtle2
# g = the different starting distance between v2 and v1, v1 is ahead
# find at what time the two will be equal distance

def race(v1, v2, g):
    if v1 >= v2:
        return None
    # 1 foot per hour = .000277778
    time = g * 3600 / (v2 - v1)
    hr = time / 3600
    mn = (time % 3600) / 60
    s = time % 60
    timeRequired = [int(hr), int(mn), int(s)]
    return timeRequired

print(race(720, 850, 70))
    
    
    
