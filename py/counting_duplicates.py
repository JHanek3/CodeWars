# Task
# Return the count of distinct case-insensitive aplhabetic and numeric characters
from collections import Counter

def duplicate_count(text):
  low = text.lower()
  low_split = []
  for x in range(len(low)):
    low_split.append(low[x])
  c = Counter(low_split)

  sum = 0
  for value in c.values():
    if value > 1:
      sum += 1
  return sum

print(duplicate_count("abcde"))
print(duplicate_count("aabbcde"))
print(duplicate_count("aabBcde"))
print(duplicate_count("indivisibility"))
print(duplicate_count("Indivisibilities"))
print(duplicate_count("aA11"))
print(duplicate_count("ABBA"))