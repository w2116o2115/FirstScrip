__author__ = 'zw'
#


import time
point = 0#文件指针
blk_set = set()
while True:
    ips =[]#存放所有的ip地址
    with open('assess.log') as f:
        f.seek(point)
        for line in f:
            ip = line.split()[0]
            ips.append(ip)
            if ips.count(ip)>199:
                blk_set.add(ip)
                print('已经把%s加入黑名单'%ip)
        point = f.tell()
        time.sleep(60)
