__author__ = 'zw'
#添加商品
# commodity=input("请输入商品名称")

def is_float(s):
        '''
        这个函数是用来判断传入的是否为小数,包括正小数和负小数三
        :param s :传入一个字符串
        :return: True or False
        '''
        s = str(s)
        if s.isdigit():
            return False
        else:
            if s.count('.') ==1: #判断小数点个数
                sl = s.split('.') #分割字符串
                left =sl[0] #小数点前面的
                right = sl[1] #小数点后面的
                if left.startswith('-') and left.count('-')==1 and right.isdigit():
                    lleft = left.split('-')[1] ##按照负号分割然后取负号后面的数
                    if lleft.isdigit():
                        return True  #负小数
                    else:
                        return False
                elif left.isdigit() and right.isdigit():
                    return True  # 正小数

                else:
                    return False
            else:
                return False

def commodity_price():
    price=str(input("请输入商品价格"))
    if price.isdigit():
        print('商品价格为整数')
        return price
    else:
        is_price = is_float(price)
        if(is_price):
            print('商品价格为小数')
            return price
        else:
            print('输入的小数错误请重新输入')
            commodity_price()

with open('commodity.txt','a+') as f:
    f.write(str(commodity_price())+'\n')
# number=input("请输入商品数量")

# couler=input("请输入商品颜色")
# def commodity_add():
#     with open(commodity.txt,'a+') as f:
#     f.write('商品名称':commodity,'价格':price,'数量':number,'颜色',couler)





