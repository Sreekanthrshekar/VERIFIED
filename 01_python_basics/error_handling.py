
#overcome TypeError
'''This documentation deals with handling errors gracefully'''

try:
    for i in ['a','b','c']:
        print (i**2)
except TypeError:
    print("The list should contain numerical values")


print('This line will only be executed if the TypeError is handled')


# overcome ZeroDivisionError

try:
    VAR_1 = 5
    VAR_2 = 0

    VAR_3 = VAR_1/VAR_2
except ZeroDivisionError:
    print('VAR_2 cannot be assigned to zero')
finally:
    print("All Done")


print('This line will only be executed if the ZeroDivisionError is handled')

#error handling with user input inside a function using try and except

def ask_for_square():
    '''This function asks for an integer and returns the squared value'''

    while True:
        try:
            num = int(input("Please enter a number to get back its square: "))
            squar = num**2
            return f'square of the number given is: {squar}'

        except ValueError:
            print("what you have entered is not a number")




print(ask_for_square())

#error handling with user input inside a function using try, except and else

def ask_for_cube():
    '''This function asks for an integer and returns the cubed value'''
    while True:
        try:
            num = int(input("Please enter a number to get back its cube: "))

        except ValueError:
            print("what you have entered is not a number")
            continue
        else:
            break



    cub = num**3
    return f'cube of the number given is: {cub}'


print(ask_for_cube())
