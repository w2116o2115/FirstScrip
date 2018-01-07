__author__ = 'zw'
#从users.txt取用户名和密码
f=open('users.txt')
#myname=f.readlines()
# while True:
#     name=input('用户名：').strip()
#     password=input('密码：').strip()
#     if name:
#         for i in f.readlines():
#             print(i)
#             b=i.split(':')
#             print(b)
#             if name in b:
#                 j=b.index(name)
#                 if password:
#                     if password==b[j+1]:
#                         print('登录成功！')
#                         break
#                     else:
#                         print('密码输入错误！')
#                 else:
#                     print('请输入密码！')
#             else:
#                 print('请先注册信息！')
#     else:
#          print('用户名不能为空！')

for line in f:
    ln=line.split(':')
    print('name:',ln[0])
    print('password:',ln[1])
f.close()

