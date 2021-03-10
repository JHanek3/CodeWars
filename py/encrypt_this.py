# Task
# Message is a string of space separated words
# The first letter needs to be converted to its ASCII, the second letter needs to be witched with the last letter
# python strings are IMMUTABLE BIG LAME

# def encrypt_this(text):
  # fin_array = list(text)
  # fin_array[0] = str(ord(fin_array[0]))
  # if ' ' not in fin_array:
  #   fin_array[1], fin_array[-1] = fin_array[-1], fin_array[1]
  # else:
  #   fin_string = ''.join(fin_array)
  #   fin_array = fin_string.split(' ')
  #   for x in fin_array:
  #     print(x[1])
  
  # print(fin_array)
  # fin_array = []
  # if text == "":
  #   return text
  # for x in text:
  #   fin_array.append(x)
  
  # for x in fin_array:
  #   if fin_array.index(x) == 0:
  #     fin_array[0] = ord(fin_array[0])
  #   elif x == ' ':
  #     spaceIndex = fin_array.index(x)
  #     fin_array[spaceIndex + 1] = ord(fin_array[spaceIndex + 1])
  #   else:
  #     continue
  
  # if ' ' not in fin_array:
  #   switch1 = fin_array[1]
  #   switch2 = fin_array[-1]
  #   fin_array[1] = switch2
  #   fin_array[-1] = switch1
  # else:
  #   fin_array.append(' ')
  #   for x in range(len(fin_array)):
  #     if fin_array[x] == ' ' :
        

  
  # print(fin_array)
  # for x in range(len(fin_array)):
  #   fin_array[x][0] = 'Ham';
  
  # for x in fin_array:
  #   print(fin_array)
  #   if len(fin_array) == 1:
  #     fin_array[0] = str(ord(fin_array[0]))
  
  
  # ele1 = fin_array.pop(1)
  # ele2 = fin_array.pop()
  # # print(ele1)
  # # print(ele2)
  # fin_array.insert(1, ele2);
  # fin_array.append(ele1);
  
  # fin_string = "".join(fin_array)

  # return fin_string

# Totally cheated, needed to see how to solve this
def encrypt_this(text):
  words = text.split(" ")
  res = []
  for i in words:
    new = ""
    temp = ""
    for j in range(len(i)):
      if j == 0:
        new += str(ord(i[j]))
      elif j == 1:
        temp = i[j]
        new += i[-1]
      elif j == len(i) - 1:
        new += temp
      else:
        new += i[j]
    res.append(new)
  return " ".join(list(filter(None, res)))

# I get it, but I dont think I ever would've been able to get to this solution without serious manhours


print(encrypt_this("Hello"))
print(encrypt_this("good"))
print(encrypt_this("hello world"))