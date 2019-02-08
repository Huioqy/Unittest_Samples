# -*- coding: utf-8 -*-

import unittest
from mathfunc import *


class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    # before each test
    def setUp(self):
        print ("do something before test.Prepare environment.")

    # after each test
    def tearDown(self):
        print ("do something after test.Clean up.")

    @classmethod
    def setUpClass(cls):
        print ("This setUpClass() method only called once.")

    @classmethod
    def tearDownClass(cls):
        print ("This tearDownClass() method only called once too.")

    # each test should start with "test" so that it can be recognized by unittest library
    # the tests may not be implemented in the order we write

    def test_add(self):
        """Test method add(a, b)"""
        print ("add")
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        print("minus")
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        print("multi")
        self.assertEqual(6, multi(2, 3))

    # Skip a test case
    # unittest.skip(reason)
    # unittest.skipIf(condition, reason) skip when condition=True
    # unittest.skipUnless(condition, reason) skip when condition=False
    # @unittest.skip("I don't want to run this case.")
    def test_divide(self):
        """Test method divide(a, b)"""
        #self.skipTest('Do not run this.')
        print("divide")
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))

if __name__ == '__main__':
    unittest.main(verbosity=2) # verbosity=2 gives a detailed report
