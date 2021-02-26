# Task
# Your goal is to implement a difference function, which subtracts one list from another, remove all values in list b
def array_diff(a, b):
  fin = []
  for x in a:
    if x not in b:
      fin.append(x)
  return fin


array_diff([1,2], [1, 3])
array_diff([1,2,2,2,3],[2])