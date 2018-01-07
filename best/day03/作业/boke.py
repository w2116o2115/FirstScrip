# name='  a b c  \n'
# print(name.strip()) #默认去掉左边的空格和换行符
# print(name.rstrip())#默认去掉右边的空格和换行符
# print(name.lstrip())#默认去掉两边的空格和换行符
# name="lily lilei"
# print(name.upper())#把所有字母变成大写
# print(name.lower())#把所有字母变成小写
# print(name.capitalize())#把首字母变成大写，其余转变成小写
# print(name.title())#把每个单词的首字母大写，其余转变成小写
# print(name.islower())#是否全是小写
# print(name.isupper())#是否全是大写
# print(name.istitle())#是否每个单词的首字母大写
# print(name.isalnum())#是否包含数字或字母
# print(name.isalpha())#是否全是是英文字母
# name1='lily zhaosi wangwu'
# name2='zhaosi'
#
# # print(name.replace('lily','zhaosi'))
# print(name1.find(name2))  # 从下标0开始，查找在字符串里第一个出现的子串
# print(name1.find(name2,5))# 从下标5开始，查找在字符串里第一个出现的子串
# print(name1.find(name2,6))# 从下标6开始，查找在字符串里第一个出现的子串,如果不存在，返回-1

# name1='lily zhaosi wangwu'
# name2='zhaosi'
# print(name1.index(name2))  # 从下标0开始，查找在字符串里第一个出现的子串
# print(name1.index(name2,5))# 从下标5开始，查找在字符串里第一个出现的子串
# print(name1.index(name2,6))# 从下标6开始，查找在字符串里第一个出现的子串,如果不存在，返回-1

# name1='lily zhaosi wangwu'
# sub='w'
# print(name1.count(sub,5,16))

# site = {"name": "菜鸟教程", "url": "www.runoob.com"}
# print("网站名：{name}, 地址 {url}".format(**site))

# str='lilly'
# print(str.center(20,'*'))

# str = "-";
# seq = ("1", "b", "c"); # 字符串序列
# print (str.join( seq ));