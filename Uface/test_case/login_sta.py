import sys
sys.path.append("C:\\Users\\uni-ubi\\PycharmProjects\\Android_app\\Uface\\test_case")
from models import myunit
from page_obj.loginPage import login
import unittest
from time import sleep

class loginTest(myunit.MyTest):

    def test_login1(self):
        """邮箱和密码文本提示,登入成功"""
        sleep(3)
        login(self.driver).guide()
        print(login(self.driver).getSize()[0])
        print(login(self.driver).getSize()[1])
        email_text=login(self.driver).email_text()
        password_text = login(self.driver).password_text()
        print(password_text)
        self.assertEqual(email_text,"请输入用户名，邮箱/手机号")
        #self.assertEqual(password_text,"6-16位数字/字母/符号")
        login(self.driver).login("18768172337", "172337")







if __name__=="__main__":
    unittest.main()