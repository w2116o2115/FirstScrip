__author__ = 'zw'
f=open('笔记','a+')
for i in f:
    print(i)
f.seek(0)#光标移到最前，移动指针的时候，只对读好使，对写不好使
f.truncate()#清空文件内容
f.tell()#查看当前文件指针的位置
print(f.read())#读取全部内容
#file() #python2里面
print(f.readline())#只读取一行内容
print(f.readlines())#读取文件里面所有的内容，吧文件里面每一行内容放到一个list

names=[]
f.write('****'+‘\n’)
f.writelines(names) #写 时候，传入一个可迭代的对象
f.close()




#文件打开有3种方式
# 读 r #如果打开的文件没有指定模式，那么默认读
#读写 r+ #读写模式，只要沾上r，文件不存在的时候，打开都会报错
# 写 w #w模式会清空原有文件内容
#写读w+ #写读模式，只要沾上w，他会把文件内容清空
# 追加 a #
#追加读写 a+ #文件指针指向最后，指针调整移到最前面，f.seek(0)