# coding=utf8
import random
number=[]
#数字
for i in range(48,58):
    number.append(chr(i))
#大写字母
for j in range(65,91):
    number.append(chr(j))
#小写字母
for k in range(97,123):
    number.append(chr(k))
print(number)

f=open('radom.txt','a+')
for i in range(9):
    for j in range(8):
        f.write(random.choice(number))
    f.write('\n')

f.close()
