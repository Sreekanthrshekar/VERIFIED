'''This documentation demonstrates use of assert statement in python'''



# application of assert statement
watch = {'name':'Titan','price':12500}
DISCOUNT = 0.25

def apply_discount(product, discount):
    '''This function takes in two arguments:
    a dictionary 'product' and 'discount' value in decimal and return the price'''
    price = float(product['price']*(1.0-discount))
    return price

print(apply_discount(watch,DISCOUNT))


def apply_discount_new(product, discount):
    '''This function takes in two arguments:
    a dictionary 'product' and 'discount' value in decimal and return the price'''
    price = float(product['price']*(1.0-discount))
    assert 0 <= price <= product['price'], 'For the given discount, price is less than zero'
    return price


print(apply_discount_new(watch,DISCOUNT))


# Issue with assert inside tuple

NUMBER = 4977211491775

def multiple_of_seven(num):
    '''This function takes in a number and checks whether it is a multiple of seven'''
    assert (num%7 == 0, 'This is not a multiple of seven') # assertion will always be true
    return f"{num} is multiple of seven"

print(multiple_of_seven(NUMBER))

def multiple_of_seven_1(num):
    '''This function takes in a number and checks whether it is a multiple of seven'''
    assert num%7 == 0, 'This is not a multiple of seven' 
    return f"{num} is multiple of seven"

print(multiple_of_seven_1(NUMBER))
