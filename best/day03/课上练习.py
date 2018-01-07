__author__ = 'zw'
#注册，死循环


#账号、密码、密码确认
#非空
#已经存在的不能注册
# all_user = {'lily':123,'zhaosi':123}
# while True:
#     username = input('username:').strip()
#     pwd = input('pwd:').strip()
#     cpwd = input('cpwd').strip()
#     if username and pwd and cpwd:
#         if username in all_user:
#             print('用户名已经存在，请重新输入')
#         else:
#             if pwd==cpwd:
#                 all_user[username]=pwd
#                 print('注册成功')
#                 break
#             else:
#                 print('两次输入密码不一致')
#     else:
#         print('账号密码不能为空')



#登录
#非空
#如输入用户名不存在，提示
all_user = {'lily':123,'zhaosi':123}
while True:
    username = input('username:').strip()
    pwd = input('pwd:').strip()
    if username and pwd:
        if username in all_user:
            if all_user[username]==pwd:
                print('登录成功')
            else:
                print('密码错误')
        else:
            print('用户名不存在')

    else:
        print('输入用户名密码为空')
