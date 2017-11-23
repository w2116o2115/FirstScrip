# -*- coding: utf-8 -*-

import unittest
from test_mathfunc import TestMathFunc

"""
我们怎么控制用例执行的顺序呢？（这里的示例中的几个测试方法并没有一定关系，
但之后你写的用例可能会有先后关系，需要先执行方法A，再执行方法B），我们就
要用到TestSuite了。我们添加到TestSuite中的case是会按照添加的顺序执行的。
"""

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


"""
上面用了TestSuite的 addTests() 方法，并直接传入了TestCase列表，我们还可以：
"""
# 直接用addTest方法添加单个TestCase
suite = unittest.TestSuite()
suite.addTest(TestMathFunc("test_multi"))

# 用addTests + TestLoader
# loadTestsFromName()，传入'模块名.TestCase名'
suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))
suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))  # loadTestsFromNames()，类似，传入列表

# loadTestsFromTestCase()，传入TestCase
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))