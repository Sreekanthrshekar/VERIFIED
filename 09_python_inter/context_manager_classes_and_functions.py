'''This document demonstrates creating custom classes and functions
which has the functionality of 'with' '''

from contextlib import contextmanager

# custom class having 'with' functionality

class ManagedFile():
    '''This class has 'with' functionality '''

    def __init__(self,name,mode):
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.name,self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.file:
            self.file.close()

# custom function having 'with' functionality

@contextmanager
def managed_file(name, mode):
    ''' This function has 'with' functionality '''

    try:
        fil = open(name,mode)
        yield fil

    finally:
        fil.close()


if __name__ == '__main__':

 # testing custom class

    with ManagedFile('hello.txt','w') as file_name:
        file_name.write('hello, world!\n')
        file_name.write('ok,bye!\n')

# testing custom function

    with managed_file('hello.txt','w') as f:
        f.write('This is an overwritten sentence.\n')
        f.write('Thanks again..\n')
