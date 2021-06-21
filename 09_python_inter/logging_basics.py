''' This document demonstrates logging basics '''

import logging as logging

# FIVE LOGGING LEVELS:

# DEBUG: Detailed information, typically of interest only when diagnosing problems

# INFO: Confirmation that things are working as expected.

# WARNING:    An indication that something unexpected happened, 
            # or indicative of some problem in near future.
            # (e.g., 'disk space low')
            # The software is still working as expected.

# ERROR:   Due to a more serious problem, 
         # the software has not been able to perform some function.

# CRITICAL:   A serious error, indicating that the program itself may be
            # unable to continue running.



logging.basicConfig(filename = './09_python_inter/arith.log',level=logging.DEBUG)

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

NUM_1 =100
NUM_2 =20

add_result = add(NUM_1,NUM_2)
logging.debug(f"Add: {NUM_1} + {NUM_2} = {add_result}")

sub_result = subtract(NUM_1,NUM_2)
logging.debug(f"Subtract: {NUM_1} - {NUM_2} = {sub_result}")

mul_result = multiply(NUM_1,NUM_2)
logging.debug(f"Multiply: {NUM_1} * {NUM_2} = {mul_result}")

div_result = divide(NUM_1,NUM_2)
logging.debug(f"Divide: {NUM_1} / {NUM_2} = {div_result}")


