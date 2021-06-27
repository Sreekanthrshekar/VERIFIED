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



# a simple custom decorator message

def decorator_func1(original_func):
    ''' decorator function '''
    def wrapper_func1():
        ''' wrapper function '''
        print('This is additionally added by the wrapper function')
        return original_func()
    return wrapper_func1


def display1():
    print('display function ran')

dec_display = decorator_func1(display1)
dec_display()

# @decorator_func above display2 is same as "display2 = decorator_func(display2)""

@decorator_func1
def display2():
    print('display function is being run here')

display2()

# original function with arguments

def display_info1(name,age):
    print(f'display_info ran with arguments ({name}, {age})')

display_info1('John', 25)

# added *args, **kwargs to wrapper and original function to facilitate
# original function with arguments

def decorator_func2(original_func):
    ''' decorator function '''
    def wrapper_func2(*args,**kwargs):
        ''' wrapper function '''
        print('This is additionally added by the wrapper function')
        return original_func(*args,**kwargs)
    return wrapper_func2

@decorator_func2
def display_info2(name,age):
    ''' This display function has arguments '''
    print(f'display_info2 ran with the arguments ({name}, {age})')

display_info2('Jane', 21)

# first decorator doesn't work on functions with arguments

@decorator_func1
def display_info3(name,age):
    ''' This display function has arguments '''
    print(f'display_info3 ran with the arguments ({name}, {age})')

#display_info3('Jane', 21)  # uncomment to run this & find that it doesn't work

# CLASSES AS DECORATORS

class decorator_class(object):
    ''' This is a decorator class '''
    
    def __init__(self, original_func):
        self.original_func = original_func
        
    # mimicking wrapper adding functionality using call method
    
    def __call__(self,*args,**kwargs):
        print('call method executed this line')
        return self.original_func(*args,**kwargs)
    

@decorator_class
def display3():
    print('display3 function is being run here')

display3()

# original function with arguments
@decorator_class
def display_info4(name,age):
    print(f'display_info4 ran with arguments ({name}, {age})')

display_info4('John', 25)
