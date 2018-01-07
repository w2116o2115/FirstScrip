__author__ = 'zw'
# key=value
d={'name':'lily','age':18,'sex':' 男','money':2000}
#取值方便、速度快

#查，两种方式，key或get
print(d['name'])
#print(d['haha'])#如果不存在的key。会报错
print(d.get('haha'))#如果不存在的key，会返回None
#print(d.get('haha',‘找不到‘))#get后可加默认值

#增加
d['high']=198
d.setdefault('weight',130)
print(d)
#修改
d['high']=200#如果这个key存在的话，修改他的值，如果key不存在的话，新增一个
#删除
d.pop('high')#删除某个key
d.popitem()#随机删除一个
del d['weight']
d.clear()#清空字典
print(d)

print(d.keys())#获取所有的key
print(d.values())#获取所有的value

#d.hash_key('weight')#python2里面字典有个方法，有没有这个key
if 'weight' in d:#判断key是否在这个字典里

#同时遍历key和value
for i,j in d.items():
    print(i,j)

print(d.items())#是把字典的k和v转成一个二维数组

for k in d:# 用此方法取值方法性能最好,通过取key打印出value
    print(k,d[k])
