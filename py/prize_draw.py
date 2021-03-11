# Task
# To participate in a prize draw each one gives his/her firstname.
# Each letter of a firstname has a value which is its rank in the English alphabet. A and a have rank 1, B and b rank 2 and so on.
# The length of the firstname is added to the sum of these ranks hence a number som.
# An array of random weights is linked to the firstnames and each som is multiplied by its corresponding weight to get what they call a winning number.
# Now one can sort the firstnames in decreasing order of the winning numbers. When two people have the same winning number sort them alphabetically by their firstnames.
# return: the firstname of the participant whose rank is n (ranks are numbered from 1)

def rank(st, we, n):
  str_array = st.split(',')
  part_dict = {}

  if st == "":
    return "No participants"
  
  if n > len(str_array):
    return "Not enough participants"
  
  for x in str_array:
    part_dict[x.lower()] = 0
  
  for key, value in  part_dict.items():
    sum = 0
    for letter in range(0, len(key)):
      sum += ord(key[letter])- 96
    part_dict[key] = sum + len(key)
  
  iterator = 0
  for key, value in  part_dict.items():
    part_dict[key] = value * we[iterator]
    iterator += 1
  
  res = {val[0] : val[1] for val in sorted(part_dict.items(), key = lambda x: (-x[1], x[0]))}

  parser = 1
  winner = ""
  for key in res.keys():
    if parser == n:
      winner = key
      parser += 1
    else:
      parser += 1
  
  for x in str_array:
    if x.lower() == winner:
      return x
  
print(rank("COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH", [1, 4, 4, 5, 2, 1], 4))
print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4))
print(rank("Lagon,Lily", [1, 5], 2))
print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8))
print(rank("", [4, 2, 1, 4, 3, 1, 2], 6))