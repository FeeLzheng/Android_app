import sys
sys.path.append("C:\\Users\\uni-ubi\\PycharmProjects\\Android_app\\Uface\\test_case\\page_obj")
from base import Page
from appium.webdriver.common.mobileby import By
from time import sleep


class login(Page):

    title_loc=(By.CLASS_NAME,"android.widget.TextView")
    email_loc=(By.ID,"com.uniubi.attendance:id/et_login_username")
    password_loc=(By.ID,"com.uniubi.attendance:id/et_login_passward")
    login_button_loc=(By.ID,"com.uniubi.attendance:id/bt_login_enter")
    forgetPassword_loc=(By.ID,"com.uniubi.attendance:id/tv_lost_found")

    guideButton_loc=(By.ID,"com.uniubi.attendance:id/bt_guide")

#标题
    def title_text(self):
        return self.find_element(*self.title_loc).text

#用户名提示
    def email_text(self):
        return self.find_element(*self.email_loc).text

#填写用户名
    def email(self,email):
        self.find_element(*self.email_loc).click()
        self.find_element(*self.email_loc).clear()
        self.find_element(*self.email_loc).send_keys(email)

#密码提示

    def password_text(self):
        return self.find_element(*self.password_loc).text

#填写密码
    def password(self,password):
        self.find_element(*self.password_loc).click()
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

#点击登陆按钮

    def loginButton(self):
        self.find_element(*self.login_button_loc).click()


#点击找回密码

    def forgetPassword(self):
        self.find_element(*self.forgetPassword_loc).click()


#安装后引导页
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return(x,y)


    def swipeLeft(self,t):
        x1 = int(self.getSize()[0] * 0.85)
        y1 = int(self.getSize()[1] * 0.5)
        x2 = int(self.getSize()[0] * 0.1)
        self.driver.swipe(x1,y1,x2,y1,t)

#点击体验按钮
    def guideButton(self):
        self.find_element(*self.guideButton_loc).click()

#统一进入引导页
    def guide(self):
        sleep(5)
        self.swipeLeft(1000)
        sleep(2)
        self.swipeLeft(1000)
        sleep(2)
        self.swipeLeft(1000)
        sleep(2)
        self.guideButton()
        sleep(1)

#统一登入接口
    def login(self,email,password):
        sleep(5)
        self.email(email)
        self.password(password)
        sleep(2)
        self.driver.keyevent(66)
        self.loginButton()







