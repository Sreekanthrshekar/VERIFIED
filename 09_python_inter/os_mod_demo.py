''' This document demonstrates various methods and attributes in os module '''

import os
from datetime import datetime

print('''
      
      ''')

# Check the current working directory
print(os.getcwd())

print('''
      
      ''')
# change working directory (to say, Desktop)

os.chdir('/home/user/Desktop')

print(os.getcwd())

print('''
      
      ''')

# List the files and folders in the current directory or any location

print(os.listdir()) # current directory

print('''
      
      ''')

print(os.listdir('/home/user/Datasets'))

print('''
      
      ''')
# Create a new folder in the current directory: Two methods

# Method 1 : create a single folder
os.mkdir('demo1')


# Method 2: create a folder and then go on to create a sub folder

os.makedirs('demo21/sub_demo1')

# REMOVE DIRECTORIES

# Method 1: remove a single directory

os.rmdir('demo1')

# Method 2: remove a dicrectory and sub directories

os.removedirs('demo21/sub_demo1')


print('''
      
      ''')

print(os.listdir())

print('''
      
      ''')

# rename files
#os.rename('Signature.jpg','My_sign.jpg')

print(os.listdir())

print('''
      
      ''')

# last modified time of a file

print(os.stat('My_sign.jpg'))

print('''
      
      ''')

last_modified_time = os.stat('My_sign.jpg').st_mtime

print(datetime.fromtimestamp(last_modified_time))

print('''
      
      ''')

# directory tree with directories and files in path

#os.walk outputs a tuple with three elements:
# dirpath,
# directories in the path,
# files in the path

for dirpath,dirnames,filenames in os.walk('/home/user/Desktop/demo2'):
    print('Current path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files:', filenames)
    print()

# access environment variables
print(os.environ.get('HOME'))

print('''
      
      ''')

# create a proper file path

filepath = os.path.join(os.environ.get('HOME'),'os_join_test_file.txt')
print(filepath)
print('''
      
      ''')
# access basename and directory name

#basename
print(os.path.basename('./temp/sree/draw.jpg'))
print('''
      
      ''')
# directory name
print(os.path.dirname('./temp/sree/draw.jpg'))
print('''
      
      ''')

#obtain both basename and directory name

dirname,basename = os.path.split('./temp/sree/draw.jpg')
print(dirname)
print(basename)
print('''
      
      ''')
# check whether path exists
print(os.path.exists('./temp/sree/draw.jpg'))

print('''
      
      ''')

#check whether it's a file or directory

print(os.path.isdir('/home/user/Desktop'))

print('''
      
      ''')
print(os.path.isfile('/home/user/Desktop'))
print('''
      
      ''')

# splitting the extension
print(os.path.splitext('./temp/sree/draw.jpg'))
