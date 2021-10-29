import os,sys,time
import unittest
sys.path.append(os.path.join(os.getcwd()))
from common import test_function
from common.log import logger
from unittestreport import  TestRunner


class TestCase(unittest.TestCase):
    def setUp(self):
        logger.info("#####测试用例开始运行#####")
        
    def test_login(self):
        res = test_function.login()
        self.assertTrue(res)

    def tearDown(self):
        logger.info("#####测试用例运行结束#####")
        
    
if __name__=="__main__":
    # print(sys.path[-1])
    # filename=time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
    # # 存放路径在目录下
    # filepath=sys.path[-1]+"\\reports\\"+"%s.html"%filename
    # print(filepath)
    # fp=open(filepath,'wb+')
    # # with open(filepath,'wb+') as fp:
    # #定义测试报告的标题与描述
    # # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'测试报告描述')
    # # print(runner.run(suite()))
    # runner = TestRunner(suite(),filename=filepath,report_dir="../reports",tester="tester",title="测试报告",desc="测试报告描述",templates=3)
    # runner.run()
    # # runner.send_email(host="smtp.qq.com", port=25, user="857330385@qq.com", password="vejungwmdhxobbej", to_addrs="857330385@qq.com")
    unittest.main()