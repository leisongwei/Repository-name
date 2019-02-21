#  coding:utf-8
import unittest
from common import HTMLTestRunner_cn

start_path = r'D:\all_test_dir\my_test_for_web_2\test_case'
rule = 'test*.py'
discover = unittest.defaultTestLoader.discover(start_dir=start_path, pattern=rule)


reportPath = 'D:\\all_test_dir\\my_test_for_web_2\\common\\' + 'report.html'
fp = open(reportPath, 'wb')
HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title='标题', description='描述报告').run(discover)

