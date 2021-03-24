# Task
# Given an array of integers, find the on that appears an odd number of times
from collections import Counter
def find_it(seq):
  c = dict(Counter(seq))
  for key, value in c.items():
    if value % 2 != 0:
      return key

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
