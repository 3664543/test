"""
========================
Author:阿杰
Time:2022/3/20 15:54
E-mail:482564719@qq.com
========================
"""
import os
# os.path.abspath : 给顶一个相对路径，获取绝对路径
p1 = os.path.abspath("..")
print(p1)

#
fp = __file__

print(fp)
"""
魔法变量：变量的值在不同的情况下是不一样的
__name__:
    启动文件中的__name__的值为__main__
    不是启动文件的情况下：打印的值为模块名

__file__:代表当前文件的文件名字(pycharm中运行的时候会显示文件的绝对路径)

"""

# 在当前文件中获取项目的根目录
# res = os.path.abspath(__file__)
# path1 = os.path.dirname(res)
# base_path = os.path.dirname(path1)


base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_path)

# 获取用例数据文件夹所在目录的绝对路径
data_dir = os.path.join(base_path,"datas")

