__author__ = 'zw'
#元组，当要求数据不可变时，可用元组

a=(1)#单个元素时为int类型
print(type(a))

b=(1,'a',2,'a')#多个元素时为元组类型
print(type(b))
print(b.count('a'))
print(b.index('a'))

