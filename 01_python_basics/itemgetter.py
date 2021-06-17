''' This document demonstrates working of itemgetter '''

from operator import itemgetter

list_1 = [23,45,67,26,6,3,88]
list_2 = ['a','b','c','d','e']

func_1 = itemgetter(1) # gets the element at index 1
func_2 = itemgetter(3) # gets the element at index 3

print(func_1(list_1))
print(func_1(list_2))

print(func_2(list_1))
print(func_2(list_2))

student_record = [ #name,marks,age
    ('Noor', 96,18),
    ('Raj', 84,17),
    ('George', 59,19),
    ('Hari',84,1),
]

student_record_new = student_record.copy()

# method 1 - sort inplace
student_record_new.sort(key = itemgetter(1), reverse=True) # sort by marks
print(student_record_new)

# method 2 -create a new sorted list

student_record_sorted = sorted(student_record,key=itemgetter(1), reverse=True)
print(student_record_sorted)

#SORT BY MULTIPLE VALUES

# Sort by higher mark, if same mark, sort in alphebetical order

# step1 - sort by secondary sorting - here alphabetical order
student_record_new_sorted = sorted(student_record,key=itemgetter(0))
print(student_record_new_sorted)

# step2 - sort by primary sorting - sorting by higher mark
student_record_new_sorted = sorted(student_record_new_sorted,key=itemgetter(1), reverse=True)
print(student_record_new_sorted)

# List of Dictionaries

users = [
    {'name': 'Antony', 'join_date': '2017-03-09', 'age':29},
    {'name': 'Britney', 'join_date': '2018-05-26', 'age':21 },
    {'name': 'Jeff', 'join_date': '2018-07-14', 'age': 30},
    {'name': 'Ned', 'join_date': '2017-02-01', 'age': 35},
    {'name': 'Earl', 'join_date': '2015-06-10', 'age':51},
]

users_sorted = sorted(users, key =itemgetter('join_date'))
print(users_sorted)
