# Task
# Write a function that takes a string and turns any words witht htat string of length 4 or greater into an abbrevation
# words should split on space and hyphens

import re

regex = re.compile('[a-z]{4,}', re.IGNORECASE)

def replace(match):
    word = match.group(0)
    return word[0] + str(len(word) - 2) + word[-1]

def abbreviate(s):
    return regex.sub(replace, s)

print(abbreviate("internationalization"))
print(abbreviate("accessibility"))
print(abbreviate("Accessibility"))
print(abbreviate("elephant-ride"))
print(abbreviate("elephant-rides are really fun!"))