# coding=utf-8
'''
这个例子展示如何在源码中嵌入doctest用例。
'>>>' 开头的行就是doctest测试用例。
不带 '>>>' 的行就是测试用例的输出。
如果实际运行的结果与期望的结果不一致，就标记为测试失败。
'''

def multiply(a, b):
    """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b
if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)

"""
上面启动测试的方式是在__main__函数中调用了doctest.testmod()方法。
如果__main__函数有其他用途，不方便调用doctest.testmod()方法，那
么可以用另外一种执行测试的方法
$ python -m doctest unnecessary_math.py
$ python -m doctest -v unnecessary_math.py
这里 -m 表示引用一个模块，-v 等价于 verbose=True。运行输出与上面基本一样。
"""