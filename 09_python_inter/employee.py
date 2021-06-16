''' This document contains the custom class Employee ''' 

class Employee():
    ''' Employee Class: 
    has methods to get email,fullname and apply salary raise '''
    
    raise_amount = 1.05 # 5% increase
    
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    @property
    def email(self):
        '''creates email from first and last name '''
        return f"{self.first_name}.{self.last_name}@gmail.com"
    
    @property
    def fullname(self):
        ''' creates full name from first and last name '''
        return f"{self.first_name} {self.last_name}"
    
    
    def apply_raise(self):
        ''' returns salary after the raise is applied '''
        self.salary = float(self.salary*self.raise_amount)
        return self.salary
