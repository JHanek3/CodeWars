# Task
# Create a NxN multiplicate table of size provided in the parameters
# size 3
# 1 2 3
# 2 4 6
# 3 6 9 

def multiplication_table(size):
  fin_array = []
  for x in range(1, size + 1):
    mult_row = []
    for y in range(1, size + 1):
      mult_row.append(x * y)
    fin_array.append(mult_row)
  return fin_array

print(multiplication_table(3))