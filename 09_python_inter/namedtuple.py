''' This document deals with NamedTuples '''

from collections import namedtuple

# Defining 'Car' datatype having 3 fields : color, milage and fueltype

Car = namedtuple('Car','color milage fueltype')
# 'color milage fueltype' is same as ['color', 'milage', 'fueltype']

my_car = Car('red','5555.56', 'petrol')

# accessing objects:
    # standard way: using index
print(my_car[0])
print(my_car[1])
print(my_car[2])
    # using unique identifiers
print(my_car.color)
print(my_car.milage)
print(my_car.fueltype)

# create ordinary tuple from namedtuple
tup = tuple(my_car)
print(tup)
