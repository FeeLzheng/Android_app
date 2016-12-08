import sys
sys.path.append("C:\\Users\\uni-ubi\\PycharmProjects\\Android_app\\Uface\\test_case\\page_obj")
from base import Page
from appium.webdriver.common.mobileby import By




class install(Page):
    install_ManagerforUnicode_loc=(By.ID,"vivo:id/vivo_adb_install_ok_button")
    def install_ManagerforUnicode(self):
        self.find_element(*self.install_ManagerforUnicode_loc).clcik()