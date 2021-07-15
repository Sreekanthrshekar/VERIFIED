''' This document deals with sorting lists, tuples and objects '''

from operator import attrgetter

li =[2,5,7,3,1,9,4,6]
# Sort the list in ascending order
# method 1
sorted_li = sorted(li)
print('sorted list:\n', sorted_li)
print('')
print('original list:\n', li)
print('')
# method 2
li.sort()
print('sorted list:\n', li )
print('')

# sorting list in descending order
li2 =[2,5,7,3,8,1,9,4,6]
# method 1
desc_sorted_li = sorted(li2, reverse=True)
print('sorted list in descending oder:\n', desc_sorted_li)
print('')
# method 2
li2.sort(reverse=True)
print('sorted list in descending oder:\n', li2)
print('')

# sorting tuple

#tuple doesn't have sort method
# so sorted() will be used

tup1= (2,5,7,3,1,9,4,6)
sorted_tup = sorted(tup1) # output will be a list; not tuple
print('sorted tuple:\n', sorted_tup)
print('')
desc_sorted_tup = sorted(tup1, reverse=True) # output will be a list; not tuple
print('sorted tuple in descending oder:\n', desc_sorted_tup)
print('')

# to obtain a tuple after sorting
tup1= (2,5,7,3,1,9,4,6)
sorted_tup = tuple(sorted(tup1)) # typecasting as tuple
print('sorted tuple:\n', sorted_tup)
print('')
desc_sorted_tup = tuple(sorted(tup1, reverse=True)) # typecasting as tuple
print('sorted tuple in descending oder:\n', desc_sorted_tup)
print('')

# sorting using absolute value
li3 =[-2,1,5,-4,8,-6]

sorted_li3 = sorted(li3)
print('sorted list:\n', sorted_li3)
print('')

sorted_li3_abs = sorted(li3, key=abs)
print('sorted list:\n', sorted_li3_abs)
print('')

# sorting class instances

class Employee:
    ''' This class represents each emplyee by their name, age and salary'''

    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)


e1 = Employee('Sree',35,2500000)
e2 = Employee('Jenny',28,900000)
e3 = Employee('David',31, 1200000)

employees = [e1,e2,e3]

# Method 1

def sort_emp(emp):
    ''' returns employee name'''
    return emp.name
sorted_employees1 = sorted(employees, key = sort_emp)

print(sorted_employees1)
print('')

# Method 2
sorted_employees2 = sorted(employees, key = lambda e:e.name)
print(sorted_employees2)
print('')

# Method 3

sorted_employees3 = sorted(employees, key=attrgetter('name'))
print(sorted_employees3)
print('')

# sorting using different attribute and in descending order
sorted_employees4 = sorted(employees, key=attrgetter('salary'), reverse=True)
print(sorted_employees4)
print('')
