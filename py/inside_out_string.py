# task
# all internal letters will move out, all external letters move toward the center
# even length all letters will move, odd length leave the middle wear it is
# only if the length of the word is 4 or more

import math
def inside_out(st):
    split = st.split(" ")
    for x in range(len(split)):
        if (len(split[x]) > 3):
            split[x] = inside_out_word(split[x])
    return (" ").join(split)

def inside_out_word(st):
    if len(st) % 2 == 0:
        half = int(len(st) / 2)
        reversed_first_half = st[:half][::-1]
        reversed_second_half = st[half:][::-1]
        return reversed_first_half + reversed_second_half
    else:
        middle = math.floor(len(st) / 2)
        middle_letter = st[middle]
        reveresed_first_half = st[:middle][::-1]
        reversed_second_half = st[middle + 1:][::-1]
        return reveresed_first_half + middle_letter + reversed_second_half

# print(inside_out("taxi"))
# print(inside_out("taxis"))
print(inside_out('man i need a taxi up to ubud'))