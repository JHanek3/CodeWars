# Task
# Count all the occuring characters in  astring

from collections import Counter

def count(string):
  return dict(Counter(string))
    # The function code should be here

print(count('aba'))