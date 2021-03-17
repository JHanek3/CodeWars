# Task
# Take in an input string and a dictionary array and return the values form the dictionary that start with the input string, if there are more than
# 5 matches, restrict your output to the first 5 results,  no matches return an empty array
# This D**CHENOZZLE didnt say all the special characters he just said $%^ were special characters, and failed test cases would just say nice try hacker with no output of why it failed
# turns out you need ALL of the special characters, cool why to say that at the problem statement

import re

def autocomplete(input_, dictionary):
  cleanInput = (re.sub(r'[-~! @#$%^&*()_+1234567890]', '', input_))

  r = re.compile(cleanInput, re.IGNORECASE)
  newList = list(filter(r.match, dictionary))
  
  if len(newList) > 5:
    finList = []
    for x in range(len(newList)):
      if x < 5:
        finList.append(newList[x])
    return finList
  
  elif len(newList) == 0:
    return []
  
  else:
    return newList


print(autocomplete('a^i', ['airplane','airport','apple','ball']))
print(autocomplete('a', ['abnormal','arm-wrestling','absolute','airplane','airport', 'angler']))
print(autocomplete('a', ['abnormal','arm-wrestling','absolute','airplane','airport', 'angler']))