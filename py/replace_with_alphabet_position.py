# Task
# Replace letters with their position in the alphabet, A,a == 1 B,a == 2

import re
def alphabet_position(text):
  fin_array = []
  cleanText = re.sub(r'[^A-Za-z]+', '', text)
 
  for x in range(len(cleanText)):
    fin_array.append(str(ord(cleanText[x].lower()) - 96))
  
  return ' '.join(fin_array)

print(alphabet_position("The sunset sets at twelve o' clock."))