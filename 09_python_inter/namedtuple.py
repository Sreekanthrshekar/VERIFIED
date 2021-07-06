''' This document deals with NamedTuples '''

from collections import namedtuple

# Defining 'Car' datatype having 3 fields : color, milage and fueltype

Car = namedtuple('Car','color milage fueltype') 
# 'color milage fueltype' is same as ['color', 'milage', 'fueltype']
