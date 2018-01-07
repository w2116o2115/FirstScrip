__author__ = 'zw'
#可变变量  list、字典
#不可变变量 元组、字符串
li = [1,1,2,3,4,5,6,7]
for i in li:
    if i%2 != 0:
        li.remove(i)
print(li)

#在循环list时不能删东西，因为下标会改变，导致结果错误
#上面问题解决办法, 深拷贝一个list，不能浅拷贝li2=li
li = [1,1,2,3,4,5,6,7]
li2=li[:]#深拷贝
for i in li2:
    if i%2 != 0:
        li.remove(i)
print(li)

#字符串这些方法都不会改变原来字符串的值
name='    best   uu\n'
new_name=name.strip() #默认去掉两边的空格和换行符
print(new_name)
new_name=name.lstrip()#默认去掉左边的空格和换行符
print(new_name)
new_name=name.rstrip()#默认去掉右边的空格和换行符
print(new_name)

new_name=name.count('u')#查看某个字符串在字符串里面出现的次数
print(new_name)

#new_name=name.capitalize(name)#首字母大写

print(name.center(20,'-'))#把字符串放中间，两边用-补齐

print(name.find('u'))#返回字符串下标，如果不存在，返回-1
print(name.index('u'))#返回字符串下标,如果不存在，报错

print(name.upper())#把所有字母变成大写
print(name.lower())#把所有字母变成小写

file_name='a.xls'
print(file_name.endswith('.xls'))#判断一个字符串是否已XX结尾

sql='select * from user'
sql.startswith('slect')#判断一个字符串是否已XX开头

f='{name} 欢迎光临'
print(f.format(name='lily'))

new_sql=sql.replace('select','update')#替换
print(new_sql)

print('122'.isdigit())#判断是否是数字

print('1a'.isalnum())#是否包含数字或字母
print('1a'.isalpha())#是否全是是英文字母

#############################
#分割
st='a,c,d,r'
print(st.split(','))#分割字符串后，返回一个list
print(st.split())#如果什么都不写的话，按照空格分割
print(st.split('c'))
#连接，int类型不能连接
slit=['a','b','c','d']
print(','.join(slit))
print(''.join(slit))

tu=(1,2,3)
print('*'.join(tu))#此方法不对，int类型不能连接

