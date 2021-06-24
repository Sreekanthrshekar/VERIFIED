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
