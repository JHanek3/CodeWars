# Task
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

def sort_array(source_array):
  odd_array = []
  for x in range(len(source_array)):
    if source_array[x] % 2 != 0:
      odd_array.append(source_array[x])
  
  backwards_pop = sorted(odd_array, reverse=True)
  
  for x in range(len(source_array)):
    if source_array[x] % 2 != 0:
      source_array[x] = backwards_pop.pop()

  return source_array

print(sort_array([7 ,1]))
print(sort_array([5, 8, 6, 3, 4]))
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))