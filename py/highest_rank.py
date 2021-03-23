# Task
# Complete the function that returns the number which is most frequent in the given input array
# If there is a tie, return the largest number around them

from collections import Counter
import operator

def highest_rank(arr):
  c = dict(Counter(arr))
  sorted_d = sorted(c.items(), key=lambda x: (x[1],x[0]), reverse=True)
  # print(sorted_d)
  return sorted_d[0][0]

print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]))
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]))
print(highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]))
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]))