'''This documentation demonstrates use of assert statement in python'''


# application of assert statement
watch = {'name':'Titan','price':12500}
DISCOUNT = 1.25

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
    assert 0 <= price <= product['price']
    return price

print(apply_discount_new(watch,DISCOUNT))
