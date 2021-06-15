'''This document demonstrates creating custom classes and functions 
which has the functionality of 'with' '''

class ManagedFile():

    def __init__(self,name,mode):
        self.name = name
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.name,self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.file:
            self.file.close()


if __name__ == '__main__':
    
    with ManagedFile('hello.txt','w') as f:
        f.write('hello, world!\n')
        f.write('ok,bye!\n')


