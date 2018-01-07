__author__ = 'zw'
fw=open('笔记')
count=1
# for f in fw:
#     print('第%s行'%count,f)
#     count+=1
for f in fw:
    f=f.strip()
    stu_lst=f.split('.')
    print(stu_lst)
