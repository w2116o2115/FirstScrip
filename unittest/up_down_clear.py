# -*- coding: utf-8 -*-

import unittest
from mathfunc import *

"""
我们添加了 setUp() 和 tearDown() 两个方法（其实是重写了TestCase的这两个方法），
这两个方法在每个测试方法执行前以及执行后执行一次，setUp用来为测试准备环境，tearDown用来清理环境

可以看到setUp和tearDown在每次执行case前后都执行了一次。
"""
class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def setUp(self):
        print "do something before test.Prepare environment."

    def tearDown(self):
        print "do something after test.Clean up."

    def test_add(self):
        """Test method add(a, b)"""
        print "add"
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        print "minus"
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        print "multi"
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        """Test method divide(a, b)"""
        print "divide"
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))

"""
如果想要在所有case执行之前准备一次环境，并在所有case执行结
束之后再清理环境，我们可以用 setUpClass() 与 tearDownClass():
"""

class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

