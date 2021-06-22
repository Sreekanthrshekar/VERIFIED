''' This document demonstrates various methods and attributes in os module '''

import os

# Check the current working directory
print(os.getcwd())

# change working directory (to say, Desktop)

os.chdir('/home/user/Desktop')

print(os.getcwd())

