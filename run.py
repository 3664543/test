"""
========================
Author:阿杰
Time:2022/3/17 10:55
E-mail:482564719@qq.com
========================
"""
import unittest
from unittestreport import TestRunner
from common.handle_path import CASES_DIR,REPORT_DIR


suite = unittest.defaultTestLoader.discover(CASES_DIR)
runner = TestRunner(suite,
                    filename = "reports.html",
                    report_dir = REPORT_DIR
                    )
runner.run()