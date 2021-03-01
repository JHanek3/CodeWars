# Task
# Create a function that can take any non-integer number and return it sorted descending

def descending_order(num):
  lis = []
  for i in str(num):
    lis.append(i)
  lis.sort(reverse = True)
  fin = int("".join(lis))
  return fin

print(descending_order(42145))