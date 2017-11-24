# coding=utf-8
"""
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列
"""
count = 0
for i in range(4):
    first = i+1
    for j in range(4):
        secound = j+1
        for k in range(4):
            third = k+1
            if first != secound and secound != third and third != first:
                count += 1
                print(str(first) + str(secound) + str(third))
print(count)