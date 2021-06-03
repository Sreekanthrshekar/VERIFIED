
#overcome TypeError

try:
    for i in ['a','b','c']: 
        print (i**2)
except TypeError:
    print("The list should contain numerical values")


print('This line will only be executed if the TypeError is handled')


# overcome ZeroDivisionError

try:
    x=5
    y=0

    z= x/y
except ZeroDivisionError:
    print('variable y cannot be assigned to zero')
finally:
    print("All Done")
    

print('This line will only be executed if the ZeroDivisionError is handled')

#error handling with user input inside a function using try and except

def ask_for_square():
    while True:
        try:
            num = int(input("Please enter a number to get back its square: "))
            sq = num**2
            return f'square of the number given is: {sq}'
        
        except ValueError:
            print("what you have entered is not a number")
      
            
            
        

print(ask_for_square())

#error handling with user input inside a function using try, except and else

def ask_for_cube():
    while True:
        try:
            num = int(input("Please enter a number to get back its cube: "))
            
        except ValueError:
            print("what you have entered is not a number")
            continue
        else: 
            break
    
    
    
    cb = num**3
    return f'cube of the number given is: {cb}'


print(ask_for_cube())