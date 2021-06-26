''' This document deals with decorators in python.

A decorator is a function that takes in another function as an argument,
adds some kind of functionality to it and returns a new function
all of this, without altering the source code of the original function
that was passed in '''


# an example of closure

def outer_func(msg):
    ''' outer function '''
    def inner_func():
        ''' inner function '''
        print(msg)
    return inner_func

wow_func = outer_func('Wow')
wow_func()

def display():
    print('display function ran')

# a simple custom decorator message

def decorator_func(original_func):
    ''' decorator function '''
    def wrapper_func():
        ''' wrapper function '''
        return original_func()
    return wrapper_func

dec_display = decorator_func(display)
dec_display()



