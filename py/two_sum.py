# Task
# Function that takes an array of numbers and a target number
# It should find two different items in the array that when added together give the target value
# The indices should be return in a tuple

def two_sum(numbers, target):
  # copy the list so we can pop values
  pop_list = numbers[:]

  for x in range(len(pop_list)):
    # remove one value a and then add it to the rest of the remaining list
    a = pop_list.pop(0)
    for y in range(len(pop_list)):
      if (a + pop_list[y] == target):
        
        # make a list and then tuple convert said list
        fin_list = []
        fin_list.append(numbers.index(a))
        

        # we get an error if list is [2, 2, 3], meaning the index will find the first guy and use him twice giving (0,0) and not (0,1)
        if (a == pop_list[y]):
          # print("They are the same")
          numbers.remove(a)
          # add one since removing from the list shifts everyone over
          fin_list.append((numbers.index(pop_list[y])) + 1)
        else:
          fin_list.append(numbers.index(pop_list[y]))
        
        # print(a + pop_list[y])
        
        return tuple(fin_list)

        
print(two_sum([1,2,3], 4))
print(two_sum([1234,5678,9012], 14690))
print(two_sum([2,2,3], 4))