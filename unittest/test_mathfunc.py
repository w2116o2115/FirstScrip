# -*- coding: utf-8 -*-

import unittest
from mathfunc import *

"""
   一个TestCase的实例就是一个测试用例。什么是测试用例呢？
   就是一个完整的测试流程，包括测试前准备环境的搭建(setUp)，
   执行测试代码(run)，以及测试后环境的还原(tearDown)。

   一个class继承了unittest.TestCase，便是一个测试用例，
   但如果其中有多个以 test 开头的方法，那么每有一个这样的方法，
   在load的时候便会生成一个TestCase实例，如：一个class中有四个
   test_xxx方法，最后在load到suite中时也有四个测试用例。

   写好TestCase，然后由TestLoader加载TestCase到TestSuite，
   然后由TextTestRunner来运行TestSuite，运行的结果保存在
   TextTestResult中，我们通过命令行或者unittest.main()执行时，
   main会调用TextTestRunner中的run来执行，或者我们可以直接通
   过TextTestRunner来执行用例。
"""
class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3, add(1, 2)) # assert 是断言 对方法结果进行判断
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))

if __name__ == '__main__':
    # unittest.main() # 用这个是最简单的，下面的用法可以同时测试多个类
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMathFunc)
    """
    在unittest.main()中加 verbosity 参数可以控制输出的错误报告的详细程度，
    默认是 1，如果设为 0，则不输出每一用例的执行结果，即没有上面的结果中
    的第1行；如果设为 2,会显示的十分详细
    """
    unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(suite))