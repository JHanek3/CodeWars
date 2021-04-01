# Task
# Return str corresponding mixed fraction
# 42 / 9  = 4 2/3
from fractions import Fraction

def mixed_fraction(s):
    numbers = s.split("/")

    if (numbers[0] == "0" and numbers[1] != "0"):
        return "0"

    if int(numbers[0]) < 0 and int(numbers[1]) < 0:
        integerVal = abs(int(numbers[0])) // abs(int(numbers[1]))
        fractionVal = abs(int(numbers[0])) / abs(int(numbers[1])) - abs(int(numbers[0])) // abs(int(numbers[1]))
        if fractionVal == 0:
            return "{}".format(integerVal)
        if integerVal == 0:
            return "{}".format(Fraction(fractionVal).limit_denominator(10000000))
        else:
            return "{} {}".format(integerVal, Fraction(fractionVal).limit_denominator(10000000))
    
    elif int(numbers[0]) < 0 or int(numbers[1]) < 0:
        integerVal = abs(int(numbers[0])) // abs(int(numbers[1]))
        fractionVal = abs(int(numbers[0])) / abs(int(numbers[1])) - abs(int(numbers[0])) // abs(int(numbers[1]))
        if fractionVal == 0:
            return "-{}".format(integerVal)
        
        if integerVal == 0:
            return "-{}".format(Fraction(fractionVal).limit_denominator(10000000))
        else:
            return "-{} {}".format(integerVal, Fraction(fractionVal).limit_denominator(10000000))
    
    elif int(numbers[0]) > int(numbers[1]):
        integerVal = int(numbers[0]) // int(numbers[1])
        fractionVal = int(numbers[0]) / int(numbers[1]) - int(numbers[0]) // int(numbers[1])
        
        if fractionVal == 0:
            return str(integerVal)
        else:    
            return "{} {}".format(integerVal, Fraction(fractionVal).limit_denominator(10000000))
    
    else:
        return str(Fraction(s).limit_denominator(10000000))

print(mixed_fraction("42/9"))
print(mixed_fraction("6/3"))
print(mixed_fraction("4/6"))
print(mixed_fraction('0/18891'))
print(mixed_fraction('-10/7'))
print(mixed_fraction('-22/-7'))
print(mixed_fraction('-1203207/-4576285'))
print(mixed_fraction('7086552/-9802424'))


# LOL, pays to be pretty
# from fractions import Fraction


# def mixed_fraction(s):
#     f = Fraction(*map(int, s.split('/')))
#     if f.denominator == 1: return str(f.numerator)
#     n = abs(f.numerator) / f.denominator * (1 if f.numerator > 0 else -1)
#     f = abs(f - n) if n else f - n
#     return "{} {}".format(n, f) if n else str(f)