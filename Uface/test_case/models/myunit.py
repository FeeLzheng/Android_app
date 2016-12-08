
from appium import webdriver
import unittest
from time import sleep
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class MyTest(unittest.TestCase):
    PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.5.1'
        desired_caps['deviceName'] = 'vivi-vivo_x7-a635f4b6'
        # desired_caps['app']= PATH('D:\\uni-ubi\\release.apk')
        desired_caps['appPackage'] = 'com.uniubi.attendance'
        desired_caps['appActivity'] = 'com.uniubi.attendance.Activity.SplashActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def tearDown(self):
        sleep(2)
        print("APP退出")
        self.driver.quit()


