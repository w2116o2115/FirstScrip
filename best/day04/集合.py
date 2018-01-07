__author__ = 'zw'
#int string list tuple dict bool float set

#集合，天生去重，集合是无序的，无下标
s = set()#空的集合
s2 = {'1','2','3','3'}#集合天生去重
s3 = {'1','2','4','5'}
#s2.add('1')#添加值
s2.remove('1')#删值
s2.pop()#随机删除值
# print(s2)
# 交集
print(s2.intersection(s3))
print(s2 & s3)
# 并集
print(s2.union(s3))
print(s2 | s3)
# 差集
print(s2.difference(s3))#s2中不包含s3的值
print(s2 - s3)
# 对称差集

