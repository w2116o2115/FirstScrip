__author__ = 'zw'
# 一个python就是一个模块
# 三种
# 1、标准模块
#   python自带的，不需要你安装的
# 2、第三方模块
#   需要安装别人提供的，
#   例如：redis
#   自动安装：进入cmd，执行pip install redis
#     手动安装：百度搜索python操作XXX，
#       下载安装包，解压，
#       在命令行里面进入到这个解压之后的目录（进入解压后的目录，shift+点击右键，打开cmd）
#       执行python setup.py install
# 3、自己写的
#   自己写的python文件

# import 模块名 导入一个文件，导入文件的实质是把这个python运行一次
# import 在导入文件时候，首先从当前目录下找这个文件。
#        其次从python的环境变量里面找，就是让一个命令在任何目录下都可以执行
import sys
print(sys.path)#查看当前系统的环境变量