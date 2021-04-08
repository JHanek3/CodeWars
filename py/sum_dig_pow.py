# Task
# Find numbers in the range that follow
# 89 = 8^1 + 9^2 and 135 = 1^1 + 3^2 + 5^3 
def sum_dig_pow(a, b):
    fin_array = []
    for x in range(a, b + 1):
        digits = [int(y) for y in str(x)]
        power = 1
        sum = 0
        for i in range(len(digits)):
            sum += digits[i] ** power
            power += 1
        if sum == x:
            fin_array.append(x)
    return fin_array
    
print(sum_dig_pow(1,10))
print(sum_dig_pow(1, 100))
print(sum_dig_pow(10, 89))
print(sum_dig_pow(10, 100))
print(sum_dig_pow(90, 100))
print(sum_dig_pow(89, 135))