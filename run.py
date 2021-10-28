import os,sys,time
import unittest
from unittest import case
from unittestreport import  TestRunner

now_path = os.path.split(os.path.realpath(__file__))[0]

def readcase():
    suite =unittest.TestSuite()
    with open("caselist.txt","r")as f:
        for case in f.readlines():
            case = case.rstrip("\n")
            if "\\" in case:
                case = case.split("\\")[-1]
            # 此处注意，要想拿到所有的testcase必须在每个文件夹中有一个__init__.py文件引导，否则无法获取。
            suite_case=unittest.defaultTestLoader.discover(now_path+"\\testCase", pattern=case+".py")
            suite.addTest(suite_case)
    return suite

def run():
    suite = readcase()
    # 仅运行
    # unittest.TextTestRunner(verbosity=2).run(readcase()) 
    filename="%s.html"%(time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime()))
    # 存放路径在目录下
    filepath=now_path+"\\reports\\"
    # print(filepath)
    #定义测试报告的标题与描述
    runner = TestRunner(suite=suite,filename=filename,report_dir=filepath,tester="tester",title="测试报告",desc="测试报告描述",templates=3)
    #用例失败重跑一次
    runner.run(count=1)
    # #发送邮件
    # runner.send_email(host="smtp.qq.com", port=25, user="857330385@qq.com", password="vejungwmdhxobbej", to_addrs="857330385@qq.com")


if __name__=="__main__":
    # readcase()
    # a = os.path.split(os.path.realpath(__file__))[0]
    # print(a)
    run()
    # suite=unittest.defaultTestLoader.discover(now_path+"\\testCase", pattern="*.py")
    # print(suite)