__author__ = 'zw'
#简单粗暴的方法，把文件读到之后修改，修改后再写入，弊端，文件量大的话占内存
# with open('geci','a+') as f:
#     f.seek(0)
#     all = f.read()
#     new_all=all.replace('一'，‘二’)
#     f.seek(0)
#     f.truncate()#清空文件内容，记得把指针移到头
#     f.write(new_all)
#     f.flush()

#一行一行处理
#os模块提供了处理文件的方法
# import os
# with open('f1') as f,open('ff','w') as f2:
# #    f.seek(0)
#     for line in f:
#         new_line=line.replace('三','是')
#         f2.write(new_line)
# os.remove('f1')#删文件
# os.rename('ff','f1')#改名

a=['qqq\n','eee\n','qqq']
f=open('f1','w')
for i in a:
    b=i.replace('1','2')
    f.write(b)
f.write('aaa')

