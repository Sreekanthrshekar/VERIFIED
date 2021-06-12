'''This documentation is for demonstating vaious I/O methods for txt files'''

myfile = open('/home/user/Verified/01_python_basics/test.txt')

# read() method
print(myfile.read())

# readlines() method
myfile.seek(0)
content = myfile.readlines()
print(content)

# printing out each line

for line in content:
    print(line)

# accessing each line and each word in a particular line

#accessing first line
print(content[0])

#accessing first word of first line
print(content[0][0:4])

#accessing second line
print(content[1])

#accessing the word 'purpose' in second line
print(content[1][9:16])
#closing a file
myfile.close()