''' This documentation shows how to use unpacking generalisation 
to merge two dictionaries'''

# merging two dictionaies without overlapping keys
dict_1 = {'id': 1, 'name': 'Arjun'}
dict_2 = {'pincode': 675409, 'email':'arjunks98@gmail.com'}
dict_merged_1 = {**dict_1,**dict_2}
print(dict_merged_1)

#merging two dictionaries with one overlapping key value pair
dict_3 = {'id': 2, 'name': 'Janaki'}
dict_4 = {'name': 'Janaki', 'salary': 85000}
dict_merged_2 = {**dict_3,**dict_4}
print(dict_merged_2)

# merging two dictionaries with same keys but different values
dict_5 = {'month':'March', 'salary':85000}
dict_6 = {'month':'April', 'salary':110000}
dict_merged_3 = {**dict_5,**dict_6}
print(dict_merged_3)
