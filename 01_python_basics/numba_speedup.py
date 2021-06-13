'''This documentation demonstrates the impact of jit from numba '''

import time
from numba import jit


# without jit

def power(num_1,num_2):
    '''This function takes in two arguments num_1 and num_2 and returns the output num_1^num_2'''
    return num_1**num_2

start = time.time()
power(30000000,20000000)
end = time.time()
print(end-start) #551 seconds (9+ mins)


#with jit

@jit
def power1(num_1,num_2):
    '''This function takes in two arguments num_1 and num_2 and returns the output num_1^num_2'''
    return num_1**num_2

start = time.time()
power1(30000000,20000000)
end = time.time()
print(end-start) # 0.326 seconds
