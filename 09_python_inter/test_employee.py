''' This document tests the employee module '''

import unittest
from employee import Employee



class TestEmployee(unittest.TestCase):
    ''' This class tests the methods in Employee class '''
    
    emp_1 = Employee('John','Smith', 95000.0)
    emp_2 = Employee('Sreekanth', 'Raja', 185000.0)
    
    def test_email(self):
        ''' Tests the email function '''
        self.assertEqual(self.emp_1.email,'John.Smith@gmail.com')
        self.assertEqual(self.emp_2.email,'Sreekanth.Raja@gmail.com')
        
        self.emp_1.first_name = 'Jane'
        self.emp_2.first_name = 'Gopal'
        
        self.assertEqual(self.emp_1.email,'Jane.Smith@gmail.com')
        self.assertEqual(self.emp_2.email,'Gopal.Raja@gmail.com')

    def test_fullname(self):
        ''' Tests the full name function '''
        
        self.emp_1.first_name = 'John'
        self.emp_2.first_name = 'Sreekanth'
        
        self.assertEqual(self.emp_1.fullname,'John Smith')
        self.assertEqual(self.emp_2.fullname,'Sreekanth Raja')
        
        self.emp_1.first_name = 'Jane'
        self.emp_2.first_name = 'Gopal'
        
        self.assertEqual(self.emp_1.fullname,'Jane Smith')
        self.assertEqual(self.emp_2.fullname,'Gopal Raja')
        
    def test_apply_raise(self):
        ''' Test apply_raise function '''
                
        self.emp_1.first_name = 'John'
        self.emp_2.first_name = 'Sreekanth'
        
                
        self.assertEqual(self.emp_1.apply_raise(), 99750.0)
        self.assertEqual(self.emp_2.apply_raise(), 194250.0)



if __name__ == '__main__':
    unittest.main()
