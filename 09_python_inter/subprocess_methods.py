''' This document deals with subprocess methods'''
import subprocess

print('''
     ''')

subprocess.run('ls', check=True)
print('''
     ''')

# adding additional arguments
subprocess.run(['ls','-la'], check=True)
