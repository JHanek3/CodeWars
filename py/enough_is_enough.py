# Task
# Given a list and a number N, create a new list that contains each number of lst at most 2 times without reordering

from collections import Counter

def delete_nth(order,max_e):
  fin_list = []
  d = Counter(order)
  
  for key, value in d.items():
    if value > max_e:
      d[key] = max_e
  
  for x in order:
    for key, value in d.items():
      if x == key:
        if fin_list.count(x) < max_e:
          fin_list.append(x)
      
  return fin_list
    
  

print(delete_nth ([1,1,1,1],2))
print(delete_nth ([20,37,20,21],1))
print(delete_nth ([1,1,3,3,7,2,2,2,2], 3))