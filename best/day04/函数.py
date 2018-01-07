__author__ = 'zw'
#函数

  # 函数 方法 功能
  # 说白 ，函数就是把一堆代码组合到一起，变成一个整体
  #函数不调用不会被执行
  #提高代码的复用性
  #全局变量、局部变量

#参数类型
#一、位置参数，必填参数
# def file(file_neme,content):#形参，形式参数
#     f = open(file_neme,'w')
#     f.write(content)
#     f.close()
# file('lijun','qqqqqqq')#实参，实际参数
# file('lijun','wwwwwww')

#二、默认值参数,非必填参数，传的话就用传的参数，没传就用默认值
# def file(file_neme,content=''):#形参，形式参数
#     f = open(file_neme,'a+')
#     f.write(content)
#     f.close()
# file('lijun','qqqqqqq')#实参，实际参数
# file('lijun')

#多个参数时，可用以下两种方式
#三、可变参数,多余的参数都会放到args里，args是一个元组
# def test(a,b=1,*args):#args名可以随便起，一般情况都用args
#     print('a:',a)
#     print('b:',b)
#     print('args:',args)
#     print(args[0])
# test('hahah','2','qqq','eee','444')#位置调用，b赋值2
# test(a='hahah')#关键字调用
# test(a='hahah',args="'qqq','eee','444'")#args不能用关键字调用，只能位置调用

#四、关键字参数,kwargs是一个字典
# def test(**kwargs):#kargs名可以随便起，一般情况都用args
#     print(kwargs)
# test(name='hhh')#需要用字典的形式去传参数

# 返回值
#如果想获取函数结果，必须return
#如果没有写retnrn，返回值是None
#return，函数立即结束
# def file(file_neme,content=''):#形参，形式参数
#     f = open(file_neme,'a+')
#     if content:
#         f.write(content)
#     else:
#         f.seek(0)
#         res = f.read()
#         return res
#     f.close()
# users=file('lijun','')#实参，实际参数
# print(users)

# 形参
# 实参
#全局变量、局部变量
a=100#全局
# def test():
#     #a=5 #局部变量
#     print('里面的',a)
# test()
# print('外面d',a)

#如想修改全局变量，需先声明global
# a=100#全局
# def test():
#     global a#声明全局变量
#     a=5
#     print('里面的',a)
# test()
# print('外面d',a)

#练习
#1、写一个校验字符串是否为合法的小数
#0.88
#-0.99
  #1、小数点的个数为1
  #2、小数点左边和右边都为数字，isdigit
  #3、正数、负数
def check_float(s):
    s=str(s)
    if s.count('.')==1:
        left=s.split('.')[0]
        right=s.split('.')[1]
        if left.isdigit() and right.isdigit():
            return  True
        else:
            if left.startswith('-') and left.count('-')==1:
                if left.split('-')[1].isdigit() and right.isdigit():
                    return True
    return False

print(check_float('1.789'))

