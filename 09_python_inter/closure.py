'''CLOSURE
Wikipedia  says, A closure is a recorsd storing a function together with
an environment: a mapping associating each free variable of the function
with the value or storage location to which the name was bound when the
closure was created.

A closure, unlike a plain function, allows the function to access those
captured variables through the closure's reference to them, even when
the function is invoked outside their scope'''

# Example 1 - closure without parameters

def outer_func():
    ''' outer function '''
    message = 'Hello'

    def inner_func():
        ''' inner function '''
        print(message)

    return inner_func


custom_func = outer_func()

print(custom_func.__name__)

custom_func()   # a closure : an inner function which remembers
                # and has access to variables that were present
                # in the local scope where it was created even
                # after the outer function has finished executing.

# Example 2 -  closures with parameters

def outer_func2(msg):
    ''' outer function '''
    message = msg

    def inner_func2():
        ''' inner function '''
        print(message)

    return inner_func2


wow_func = outer_func2('Wow')

wow_func()
