''' This document demonstrates various arithmatic operations between two numbers '''

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
