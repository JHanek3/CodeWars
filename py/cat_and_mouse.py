# Task
# Find out if the cat catches the mouse
import collections

def cat_mouse(x):
    if x.count(".") <= 3:
        return "Caught!"
    else:
        return "Escaped!"

print(cat_mouse('C....m'))