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

#EXAMPLE 2

# Method 1 -  usual

nums_square_1 = []
for n in nums:
    nums_square_1.append(n**2)

print(nums_square_1)

# Method 2 -  list comprehension

nums_square_2 = [n**2 for n in nums]
print(nums_square_2)

#LIST COMPREHENSION WITH CONDITION

# list of even numbers from nums

# Method 1: usual

nums_even_1 = []
for n in nums:
    if n%2 == 0:
        nums_even_1.append(n)

print(nums_even_1)

# Method 2 :  list comprehension

# step 1: write the first sentence of for loop inside a list
# nums_even_2 = [for n in nums]

# step 2: add the condition 
# nums_even_2 = [for n in nums if n%2 == 0]

# step 3: add in front of that, the result we want (here n)
# nums_copy_2 = [n for n in nums if n%2 == 0]

nums_even_2 = [n for n in nums if n%2 ==0 ]
print(nums_even_2)

# A tuple formed from each characters from two strings - nested for loops

# Method 1 - usual

my_list_1=[]
for letter in 'abcd':
    for num in '0123':
        my_list_1.append((letter, num))

print(my_list_1)

# Method 2 -  list comprehension
my_list_2 = [(letter, num) for letter in 'abcd' for num in '0123']
print(my_list_2)

