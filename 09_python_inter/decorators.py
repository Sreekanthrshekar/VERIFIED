''' This document deals with decorators in python.

A decorator is a function that takes in another function as an argument,
adds some kind of functionality to it and returns a new function
all of this, without altering the source code of the original function
that was passed in '''



def outer_func2(msg):
    ''' outer function '''
    def inner_func2():
        ''' inner function '''
        print(msg)

    return inner_func2


wow_func = outer_func2('Wow')

wow_func()