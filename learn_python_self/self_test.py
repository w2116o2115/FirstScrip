# -*- coding: utf-8 -*-
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
# 创建一个类的实体
t = Test()
#调用类中的prt方法
t.prt()
"""
从上面的例子中可以很明显的看出，self代表的是类的实例。而self.class则指向类。
"""