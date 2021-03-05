# Task
# Write a function, which changes all but the last four characters into #

def maskify(cc):
  masked = ''
  if len(cc) > 4:
    for index in range(len(cc)):
      if index < (len(cc) - 4):
        masked += '#'
      else:
        masked += cc[index]
    return masked
  else:
    return cc

print(maskify("4556364607935616"))
print(maskify("64607935616"))
print(maskify("1"))
print(maskify(""))