''' This document deals with subprocess methods'''
import subprocess

print('''
     ''')

subprocess.run('ls', check=True)
print('''
     ''')

# adding additional arguments
subprocess.run(['ls','-la'], check=True)
print('''
     ''')

# capture the output in a variable

list_dir = subprocess.run(['ls','-la'], check=True,capture_output=True)
print(list_dir.stdout) #output is captured in bytes
print('''
     ''')

# decoding the output from bytes: Method 1
print(list_dir.stdout.decode())

print('''
      
      ''')

# decoding the output from bytes: Method 2
list_dir = subprocess.run(['ls','-la'], check=True,capture_output=True,text=True)
print(list_dir.stdout)

# redirecting stdout to a file
with open('./09_python_inter/output.txt', 'w') as f:
    subprocess.run(['ls','-la'], check=True, stdout=f,text=True)
