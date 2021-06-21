''' This document demonstrates logging basics '''

def add(num_1,num_2):
    ''' Add function '''
    return num_1 + num_2

def subtract(num_1,num_2):
    ''' Subtract function '''
    return num_1 - num_2

def multiply(num_1,num_2):
    ''' Multiply function '''
    return num_1 * num_2

def divide(num_1,num_2):
    ''' Divide function '''
    if num_2 == 0:
        raise ValueError('cannot divide by zero')
    return num_1 / num_2

NUM_1 =10
NUM_2 = 5

add_result = add(NUM_1,NUM_2)
print(f"Add: {NUM_1} + {NUM_2} = {add_result}")

sub_result = subtract(NUM_1,NUM_2)
print(f"Subtract: {NUM_1} - {NUM_2} = {sub_result}")

mul_result = multiply(NUM_1,NUM_2)
print(f"Multiply: {NUM_1} * {NUM_2} = {mul_result}")

div_result = divide(NUM_1,NUM_2)
print(f"Divide: {NUM_1} / {NUM_2} = {div_result}")

