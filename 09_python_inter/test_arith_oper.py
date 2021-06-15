'''This document is used to test the arith_oper module'''

import unittest
import arith_oper

class TestArithOper(unittest.TestCase):
    '''This class has methods to test various arithmatic operations'''

    def test_add(self):
        '''test add functionality'''
        self.assertEqual(arith_oper.add(5,10), 15)
        self.assertEqual(arith_oper.add(5,-10), -5)
        self.assertEqual(arith_oper.add(2.5,10), 12.5)
        self.assertEqual(arith_oper.add(-5,10), 5)
        self.assertEqual(arith_oper.add(-5,5), 0)
        self.assertEqual(arith_oper.add(-5,-5), -10)

    def test_subtract(self):
        '''test subtract functionality'''
        self.assertEqual(arith_oper.subtract(5,10), -5)
        self.assertEqual(arith_oper.subtract(5,-10), 15)
        self.assertEqual(arith_oper.subtract(2.5,10), -7.5)
        self.assertEqual(arith_oper.subtract(-5,10), -15)
        self.assertEqual(arith_oper.subtract(-5,5), -10)
        self.assertEqual(arith_oper.subtract(-5,-5), 0)

    def test_multipy(self):
        '''test multiplication function'''
        self.assertEqual(arith_oper.multiply(5,10), 50)
        self.assertEqual(arith_oper.multiply(5,-10), -50)
        self.assertEqual(arith_oper.multiply(2.5,10), 25)
        self.assertEqual(arith_oper.multiply(-5,10), -50)
        self.assertEqual(arith_oper.multiply(-5,5), -25)
        self.assertEqual(arith_oper.multiply(-5,-5), 25)

    def test_divide(self):
        '''test division function'''
        self.assertEqual(arith_oper.divide(5,10), 0.5)
        self.assertEqual(arith_oper.divide(5,-10), -0.5)
        self.assertEqual(arith_oper.divide(2.5,10), 0.25)
        self.assertEqual(arith_oper.divide(-5,10), -0.5)
        self.assertEqual(arith_oper.divide(-5,5), -1)
        self.assertEqual(arith_oper.divide(-5,-5), 1)

        with self.assertRaises(ValueError):
            arith_oper.divide(10,0)



if __name__ == '__main__':
    unittest.main()
