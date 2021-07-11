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
print('list_dir:\n', list_dir.stdout)

print('''
      
      ''')
# alternative to capture_output
list_dir1 = subprocess.run('ls -la', check=True,stdout=subprocess.PIPE, shell=True,text=True)
print('list_dir1:\n', list_dir1.stdout)

print('''
      
      ''')
# redirecting stdout to a file
with open('./09_python_inter/output.txt', 'w') as f:
    subprocess.run(['ls','-la'], check=True, stdout=f,text=True)

print('''
      
      ''')
# checking whether external command failed
list_dir2 = subprocess.run(['ls','-la','./09_python_intere'],
                           capture_output=True, text=True)
print(list_dir2.returncode)
print(list_dir2.stderr)
print(list_dir2.stdout)

print('''
      
      ''')
# using 'check' to identify when external command fails
list_dir2 = subprocess.run(['ls','-la','./09_python_inter'],check=True,
                           capture_output=True, text=True)
print(list_dir2.returncode)
print(list_dir2.stderr)
print(list_dir2.stdout)

print('''
      
      ''')
# cat function of linux
output_string = subprocess.run('cat ./09_python_inter/demo_text.txt',check=True,
                               capture_output=True, text=True, shell=True)
print(output_string.stdout)

print('''
      
      ''')
# grep function of linux
grep_out = subprocess.run('grep -n test ./09_python_inter/demo_text.txt',check=True,
                               capture_output=True, text=True, shell=True)
print(grep_out.stdout)

print('''
      
      ''')
# pipe function of linux to combine cat and grep
grep_cat_pipe = subprocess.run('cat ./09_python_inter/demo_text.txt | grep -n test',
                               check=True,shell=True,capture_output=True, text=True)
print('Pipe:\n',grep_cat_pipe.stdout)

print('''
      
      ''')
# taking output of one command as input for another command
grep_test_output = subprocess.run('grep -n test',check=True,capture_output=True,
                                  text= True, shell=True, input=output_string.stdout)
print('taking output of another command as input:\n', grep_test_output.stdout)
