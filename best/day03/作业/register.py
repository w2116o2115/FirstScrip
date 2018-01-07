# __author__ = 'zw'
# #注册，账号密码保存到文件users.txt
f=open('users.txt','a+')
#f.close()
while True:
    name=input('用户名：').strip()
    if name:
        f.seek(0,0)
        nr=f.read()
        if name in nr:
            print('用户名已经存在！')
        else:
            password=input('密码：').strip()
            if password:
                fpd=input('重复输入密码:').strip()
                if fpd:
                    if int(password)==int(fpd):
                        print('注册成功！')
                        f.write(name)
                        f.write(':')
                        f.write(password)
                        f.write(':')
                        break
                    else:
                        print('密码与重新输入密码值不一致！')
                else:
                    print('重复输入密码不能为空！')
            else:
                print('密码不能为空！')
    else:
        print('用户名不能为空！')
f.close()
f=open('users.txt','a+')
nr=f.read()