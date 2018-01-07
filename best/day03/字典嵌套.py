__author__ = 'zw'
# key=value


stus = {
    'ybq': {
        'age': 18,
        'sex': '男',
        'addr': '昌平区',
        'money': 10000000,
        'jinku': {
            '建行卡': 80000,
            '工商卡': 800000,
            '招商卡': 8000000
        }
    },
    'tlx': {
        'age': 19,
        'sex': '女',
        'addr': '昌平区',
        'money': 10000000,
        'huazhuangpin': ['chanle','haha']
    },
    'mpp': {
        'age': 19,
        'sex': '女',
        'addr': '昌平区',
        'money': 10000000,
        "bag": {
            'lv': '一车',
            '鳄鱼':10
        }
    },
}

#计算ybq下所有银行卡的钱
count=0
for i in stus['ybq']['jinku']:
    count+=stus['ybq']['jinku'][i]
print(count)