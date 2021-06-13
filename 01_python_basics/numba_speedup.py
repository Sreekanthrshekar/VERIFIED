from numba import jit
import time

# without jit

def power(x,y):
    return x**y

start = time.time()
power(3000000,2000000)
end = time.time()
print(end-start)


#with jit

@jit
def power1(x,y):
    return x**y

start = time.time()
power1(3000000,2000000)
end = time.time()
print(end-start)
