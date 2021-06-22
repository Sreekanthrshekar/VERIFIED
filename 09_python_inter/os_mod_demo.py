''' This document demonstrates various methods and attributes in os module '''

import os

# Check the current working directory
print(os.getcwd())

# change working directory (to say, Desktop)

os.chdir('/home/user/Desktop')

print(os.getcwd())

# List the files and folders in the current directory or any location

print(os.listdir()) # current directory

print(os.listdir('/home/user/Datasets')) 

# Create a new folder in the current directory: Two methods

# Method 1 : create a single folder
os.mkdir('demo') 

# Method 2: create a folder and then go on to create a sub folder

os.makedirs('demo2/sub_demo')
