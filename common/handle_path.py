"""
========================
Author:阿杰
Time:2022/3/20 16:11
E-mail:482564719@qq.com
========================
"""
"""
此模块专门用来处理项目中的绝对路径

"""
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 用例数据所在目录


DATA_DIR = os.path.join(BASE_DIR, "datas")


# 配置文件的根目录
CONF_DIR = os.path.join(BASE_DIR, "conf")

# 日志文件所在目录
LOG_DIR = os.path.join(BASE_DIR, "logs")

# 报告所在路径
REPORT_DIR = os.path.join(BASE_DIR, "reports")

# 用例模板所在路径
CASES_DIR = os.path.join(BASE_DIR, "testcases")
