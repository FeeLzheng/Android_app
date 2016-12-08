import sys
sys.path.append("C:\\Users\\uni-ubi\\PycharmProjects\\Android_app\\Uface\\test_case")
from models import myunit
from page_obj.loginPage import login
from page_obj.attendancePage import attendance
import unittest
from time import sleep

class attendanceTest(myunit.MyTest):

    def test_attendance1(self):
        """考勤页面"""
        sleep(2)
        login(self.driver).login("18768172337", "172337")
        title=attendance(self.driver).attendanceTitle_text()
        self.assertEqual(title,"考勤")
        sleep(2)
        attendance(self.driver).attendanceDate_click()
        sleep(2)
        attendance(self.driver).attendanceToday_click()


if __name__=="__main__":
    unittest.main()