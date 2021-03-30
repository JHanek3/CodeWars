# Task 
# cut the string into chunks of size sz, ignore last chunk if its size is less than sz
# if a chunk represents an int such as the sum of cubes of its digits being divisble by two reverse the chunk, otherwise rotate it to the left by one position
# Put together these chunks and return the result as a string

from collections import deque

def revrot(strng, sz):
    if (strng == "" or sz == 0):
        return ""
    
    myChunks = [strng[i:i + sz] for i in range(0, len(strng), sz)]
    
    if len(myChunks[-1]) != sz:
        myChunks.pop()
    
    for x in range(len(myChunks)):
        sum = 0
        for y in range(0, sz):
            sum += int(myChunks[x][y]) ** 3
        if sum % 2 == 0:
            myChunks[x] = myChunks[x][::-1]
        else:
            rotator = deque(myChunks[x])
            rotator.rotate(-1)
            myChunks[x] = ''.join(rotator)
            
    return ''.join(myChunks)

print(revrot("123456987654", 6) == "234561876549")
print(revrot("123456987653", 6) == "234561356789")
print(revrot("664438769", 8) == "67834466")
print(revrot("", 8))
print(revrot("123456779", 0))