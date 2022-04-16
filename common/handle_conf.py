"""
========================
Author:阿杰
Time:2022/3/17 16:07
E-mail:482564719@qq.com
========================
"""
import os
from configparser import ConfigParser
from common.handle_path import CONF_DIR
# conf = ConfigParser()
# conf.read(r'D:\project\Python\py_test02\comfig.ini')


class Config(ConfigParser):

     def __init__(self,conf_file):

         super().__init__()
         self.read(conf_file,encoding='utf-8')


conf = Config(os.path.join(CONF_DIR,'comfig.ini'))


