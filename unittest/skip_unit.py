# -*- coding: utf-8 -*-

import unittest
from mathfunc import *

"""
如果我们临时想要跳过某个case不执行怎么办？unittest也提供了几种方法：

unittest.skip(reason)、unittest.skipIf(condition, reason)、unittest.skipUnless(condition, reason)，
skip无条件跳过，skipIf当condition为True时跳过，skipUnless当condition为False时跳过。
"""
class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""
    @unittest.skip("I don't want to run this case.")
    def test_divide(self):
        """Test method divide(a, b)"""
        print "divide"
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))