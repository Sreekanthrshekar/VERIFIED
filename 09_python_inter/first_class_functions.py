''' This document illustrates first class functions of python

First class functions:
A programming language is said to have first-class functions
if it treats functions as first-class citizens.

First-class citizens (programming):
A first class citizen (sometimes called first-class objects)
in a programming language is an entity which supports all the operations
generally available to other entities. These operations typically include
being passed as an argument, returning from a function,
and assigned to a variable.'''

# Assign a function to a variable

def square(num):
    return num**2

var_1 = square(5)

print(square) #returns memory location of the function 'square'
print(var_1) # returns the output

var_2 = square # assigning variable to function

print(square) # returns memory location of the function 'square'
print(var_2)  # returns memory location of the function 'square'

print(var_2(4)) # the variable acts as a function

# pass functions as arguments

    # creating custom map function

def my_map(func,arg_list):
    result =[]
    for i in arg_list:
        result.append(func(i))
    return result

#cross-checking my_map function

print(my_map(lambda x:x**2, [1,2,3,4]))

# creating cube function
def cube(num):
    return num**3

# passing cube function as argument

print(my_map(cube, [1,2,3,4]))