'''This documentation is for demonstating vaious I/O methods for txt files'''

myfile = open('/home/user/Verified/01_python_basics/test.txt')

# read() method
print(myfile.read())

# readlines() method
myfile.seek(0)
print(myfile.readlines())

# printing out each line 
myfile.seek(0)
for line in myfile.readlines():
    print(line)