''' This document deals with sorting lists, tuples and objects '''

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
