__author__ = 'zw'
#下标、角标、索引
#
stus=['zhangsan','lisi','wangwu']
#增加
stus.append('zhaoliu')
#改
stus[0]='lily'
print(stus)

#查看
print(stus.count('lily'))
#查看某个元素在这个里面的个数，如果该元素不存在，返回0
print(stus.index('lily'))
#找到元素的下标，如果元素不存在报错

#删除元素
stus.pop()#默认删除最后一个元素，如果指定下标，删除指定元素，如果删除不存在的下标报错
stus.remove('lisi')#删除list里面的一个元素
#pop与remove的区别：pop返回删除的元素值，remove不返回删除的元素
print(stus.pop())
print(stus)

del stus[0]#删除下标所在的元素
stus.clear()#清空整个list

stus.reverse()#反转list
stus.sort()#默认升序排序，如字段串按第一个字母排序，数字
stus.sort(reverse=True)#按降序排序

#多维数组
#二维数组  三维数组
all_nums=[123,234,[222,333,34]]
tree=[[123,234,[222,333,34,['asd',22]]]]
print(all_nums[2][0])
#函数extend()，作用是合并list
a=[1,2,3]
b=[4,5,6]
print(a.extend(b))