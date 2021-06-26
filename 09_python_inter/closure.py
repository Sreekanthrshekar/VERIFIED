'''CLOSURE
Wikipedia  says, A closure is a recorsd storing a function together with
an environment: a mapping associating each free variable of the function 
with the value or storage location to which the name was bound when the
closure was created.

A closure, unlike a plain function, allows the function to access those 
captured variables through the closure's reference to them, even when
the function is invoked outside their scope'''

# Example 1

def outer_func():
    message = 'Hello'
    
    def inner_func():
        print(message)
        
    return inner_func()


outer_func()