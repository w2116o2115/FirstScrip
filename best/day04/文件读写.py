__author__ = 'zw'
f = open('a.txt','w')
names=['a','b','c']
# for name in names:
#     f.write(name)
# f.writelines(names)#会循环对象内容，常用于写入可迭代的对象
# f.writeline()#常用于写入字符串
#
# f.flush()#立即把缓冲区里面的内容写到磁盘里面

#with自动关闭文件,可一个with打开多个文件
# with open('a.txt','w') as f1,open('b.txt','w') as f2:
#     f.write('hahha')

# rb
# wb
# ab
# 图片、音频、视频，bytes，以二进制模式打开
# f=open('5.png',rb)
#     f.write()
