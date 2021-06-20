''' This document demonstrates dictionary comprehension ''' 

names = [
    'Bruce',
    'Clark',
    'Peter',
    'Logan',
    'Wade',
    ]

heros = [
    'Batman',
    'Superman',
    'Spiderman',
    'Wolverine',
    'Deadpool',
    ]

# Create a dictionary with name names,heros as key - value pair


# Method 1 : usual method

my_dict_1 ={}

for name, hero in zip(names, heros):
    my_dict_1[name] = hero

print(my_dict_1)

# Method 2: dict comprehension

my_dict_2 = {name:hero for name,hero in zip(names,heros)}
print(my_dict_2)