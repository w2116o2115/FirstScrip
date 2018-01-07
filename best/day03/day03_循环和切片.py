__author__ = 'zw'
names=['haha','hehe']
for name in names:
    print(name)
#如果直接for循环一个list的时候。那么每次循环的值都是这个list里面的元素

nums=[1,2,3,4,5,6,7]
#切片
#就是list取值的一种方式
print(nums[1:3])
#切片是顾头部顾尾
print(nums[:3])#如果切片前面的一个值不写的话，从开头取
print(nums[0:])#如果切片后面的值不写的话，取到末尾
print(nums[:])#如果前后的值都不写，那么取全部元素

print(nums[::2])#步长，默认步长为1
print(nums[::-1])
print(nums[-1:-8:-1])
print(nums[::-2])
#步长是正数的话从左往右取
#步长是负数的话从右往左取

#切片适用于字符串
title='今天发苹果'
print(title[3:5])
for t in title:
    print(t,end="")
#函数enumerate()，可同时循环下标和元素值
for i,j in enumerate(title):
    print('%s:%s'%(i,j))
