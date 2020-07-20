import time
import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite=unittest.defaultTestLoader.discover("E:\\pythonwork\\ecshop\\testcase\\","*.py")
    file = open("E:\\pythonwork\\ecshop\\testresult\\result_.html", "wb")
    htr = HTMLTestRunner(stream=file, title="ECSHOP自动化测试报告", description="自动化用例执行情况如下：")
    htr.run(suite)
    time.sleep(3)