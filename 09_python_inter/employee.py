''' This document contains the custom class Employee '''


import logging
logging.basicConfig(filename='./09_python_inter/employee.log',level=logging.INFO,
                    format='%(levelname)s:%(message)s')


class Employee():
    ''' Employee Class: 
    has methods to get email,fullname and apply salary raise '''
    
    # Class variables
    raise_amount = 1.05 # 5% increase
    count_of_employees = 0
    
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        Employee.count_of_employees += 1
        
        logging.info('Created employee: {} {}'.format(self.first_name, self.last_name))
        logging.info('Current count of employees: {}'.format(Employee.count_of_employees))

    
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
    
    @classmethod
    def set_raise_amount(cls, raise_amount):
        cls.raise_amount = raise_amount


if __name__ == '__main__':
    emp_1 = Employee('John','Smith', 95000)
    emp_2 = Employee('Raja','Gopal', 198000)

    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)
    
    Employee.set_raise_amount(1.1)
    
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)