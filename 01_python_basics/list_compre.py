''' This document demonstrates list comprehension ''' 

nums = [1,2,3,4,5,6,7,8,9]

# want a copy of nums

# Method 1 -  usual for loop

nums_copy_1 = []
for n in nums:
    nums_copy_1.append(n)

print(nums_copy_1)

# Method 2 - list comprehension

# step 1: write the first sentence of for loop inside a list
# nums_copy_2 = [for n in nums]

# step 2: add in front of that, the result we want (here n)
# nums_copy_2 = [n for n in nums]

nums_copy_2 = [n for n in nums]
print(nums_copy_2)