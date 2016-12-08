from appium.webdriver.common.mobileby import By
from base import Page
from time import sleep
import sys
sys.path.append("C:\\Users\\uni-ubi\\PycharmProjects\\Android_app\\Uface\\test_case\\page_obj")



class attendance(Page):
#日期
    attendance_date_loc=(By.ID,"com.uniubi.attendance:id/tv_calendar_day")
#今天
    attendance_today_loc=(By.ID,"com.uniubi.attendance:id/tv_today")
#标题
    attendance_title_loc=(By.ID,"com.uniubi.attendance:id/tv_titlebar_title")
#菜单栏中的考勤
    attendance_loc=(By.ID,"com.uniubi.attendance:id/rl_work_case")


#点击日期
    def attendanceDate_click(self):
        a=self.find_elements(*self.attendance_date_loc)
        a[0].click()
        a[1].click()
        a[2].click()
        a[3].click()
        a[4].click()
        a[5].click()
        a[6].click()


#点击今天
    def attendanceToday_click(self):
        self.find_element(*self.attendance_today_loc).click()

#点击菜单栏中的考勤
    def attendacne_clcik(self):
        self.find_element(*self.attendance_loc).click()

#标题
    def attendanceTitle_text(self):
        return self.find_element(*self.attendance_title_loc).text