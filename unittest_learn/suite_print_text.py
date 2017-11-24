# -*- coding: utf-8 -*-

import unittest
from test_mathfunc import TestMathFunc

"""
用例组织好了，但结果只能输出到控制台，这样没有办法查看
之前的执行记录，我们想将结果输出到文件。很简单，看示
"""

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    with open('UnittestTextReport.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)