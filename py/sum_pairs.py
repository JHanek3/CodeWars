# Task
# Given a list of integers and a asingle sum value, return the first two values in order of appearance that add up to form the sum

def sum_pairs(nums, sum_value):
    seen = set()
    for num in nums:
        diff = sum_value - num
        if diff in seen:
            return [diff, num]
        seen.add(num)
  
  

print(sum_pairs([11, 3, 7, 5], 10))
# print(sum_pairs([4, 3, 2, 3, 4], 6))
# print(sum_pairs([0, 0, -2, 3], 2))
print(sum_pairs([10, 5, 2, 3, 7, 5], 10))