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
