from appium.webdriver.common.mobileby import By
import sys
sys.path.append("C:\\Users\\uni-ubi\\PycharmProjects\\Android_app\\Uface\\test_case\\page_obj")
from time import sleep
from base import Page
import time
import datetime


class process(Page):

    time_other=datetime.datetime.now()-datetime.timedelta(days=1)
#获取系统时间_其他请假类型
    def Systemtime1(self):
        global time_other
        time_other=datetime.datetime.now()

        return time_other
#返回其他的系统时间
    def returnSystemtime1(self):

        return time_other


#获取系统时间_补签时间
    time_resign = datetime.datetime.now() - datetime.timedelta(days=1)
    def Systemtime2(self):
        global time_resign
        time_resign = datetime.datetime.now()
        return time_resign

#返回补签的系统时间
    def returnSystemtime2(self):

        return time_resign

#出差当天系统时间
    time_outwork=datetime.date.today()
    def Systemtime3(self):
        global time_outwork
        time_outwork=datetime.date.today()
        return time_outwork

    def returnSystemtime3(self):

        return time_outwork

#出差时间加一

    time_outwork_future=datetime.date.today()

    def Systemtime5(self):
        global time_outwork_future
        time_outwork_future=datetime.date.today() + datetime.timedelta(days=1)

        return time_outwork_future

    def returnSystemtime5(self):

        return time_outwork_future
#请假当天系统时间

    time_leave=datetime.datetime.now()
    def Systemtime4(self):
        global time_leave
        time_leave=datetime.datetime.now()
        return time_leave

    def returnSystemtime4(self):

        return time_leave

#菜单栏中的流程
    prcess_loc=(By.ID,"com.uniubi.attendance:id/ll_processs")
    def process_click(self):
        self.find_element(*self.prcess_loc).click()
#请假图标
    leave_loc=(By.ID,"com.uniubi.attendance:id/ll_leave")
    def leave_click(self):
        self.find_element(*self.leave_loc).click()

#流程--请假：
    #选择请假类型
    process_type_loc=(By.ID,"com.uniubi.attendance:id/tv_select_leave_type")
    #事假
    issue_loc=(By.ID,"com.uniubi.attendance:id/tv_leave_type1")
    # 病假
    sick_loc = (By.ID, "com.uniubi.attendance:id/tv_leave_type2")
    # 年假
    annual_loc = (By.ID, "com.uniubi.attendance:id/tv_leave_type3")
    # 产假
    maternity_loc = (By.ID, "com.uniubi.attendance:id/tv_leave_type4")
    # 特殊假
    special_loc = (By.ID, "com.uniubi.attendance:id/tv_leave_type5")


#点击请假类型
    def process_type(self,i):
        self.find_element(*self.process_type_loc).click()
        path="com.uniubi.attendance:id/tv_leave_type"+str(i)
        self.driver.find_element_by_id(path).click()


 #点击开始时间
    starttime_loc=(By.ID,"com.uniubi.attendance:id/ll_leave_start")

    def starttime_click(self):
        self.find_element(*self.starttime_loc).click()
# 点击结束时间
    leaveend_loc=(By.ID,"com.uniubi.attendance:id/ll_leave_end")

    def leaveend_click(self):
        self.find_element(*self.leaveend_loc).click()



    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']

        return (x, y)
#选择开始时间
    start_time=(By.ID,"android:id/numberpicker_input")
    start_time_button=(By.ID,"android:id/button1")
    def choose_startTime(self,hour,minute):
        startTime_H = int(self.find_elements(*self.start_time)[1].text)
        startTime_M = int(self.find_elements(*self.start_time)[2].text)
    # 获取小时坐标
        x1 = int(self.getSize()[0] * 0.55)
        y1 = int(self.getSize()[1] * 0.45)
        y2 = int(self.getSize()[1] * 0.36)

    # 获取分钟坐标
        x1_M = int(self.getSize()[0] * 0.75)
        y1_M = int(self.getSize()[1] * 0.45)
        y2_M = int(self.getSize()[1] * 0.36)


        while(startTime_H != hour):
            self.driver.swipe(x1, y1, x1, y2, 500)
            sleep(1)
            startTime_H = int(self.find_elements(*self.start_time)[1].text)
        while(startTime_M != minute):
            self.driver.swipe(x1_M, y1_M, x1_M, y2, 500)
            sleep(1)
            startTime_M = int(self.find_elements(*self.start_time)[2].text)


        self.find_element(*self.start_time_button).click()

#选择离开时间
    end_time = (By.ID, "android:id/numberpicker_input")
    def choose_endTime(self,hour,minute):
        endTime_H = int(self.find_elements(*self.end_time)[1].text)
        endTime_M = int(self.find_elements(*self.end_time)[2].text)
    # 获取小时坐标

        x1 = int(self.getSize()[0] * 0.55)
        y1 = int(self.getSize()[1] * 0.45)
        y2 = int(self.getSize()[1] * 0.36)


    # 获取分钟坐标
        x1_M = int(self.getSize()[0] * 0.75)
        y1_M = int(self.getSize()[1] * 0.45)
        y2_M = int(self.getSize()[1] * 0.36)
        while(endTime_H!= hour):
            self.driver.swipe(x1, y1, x1, y2, 500)
            sleep(1)
            endTime_H = int(self.find_elements(*self.end_time)[1].text)
        while(endTime_M!= minute):
            self.driver.swipe(x1_M, y1_M, x1_M, y2_M, 500)

            endTime_M = int(self.find_elements(*self.end_time)[2].text)
        self.find_element(*self.start_time_button).click()

#备注
    reason_leave_loc=(By.ID,"com.uniubi.attendance:id/et_leave_reason")
    def reason_leave(self,reason):
        self.find_element(*self.reason_leave_loc).click()
        sleep(1)
        self.find_element(*self.reason_leave_loc).send_keys(reason)





#点击抄送
    copyTo_loc=(By.ID,"com.uniubi.attendance:id/tv_copy_to")
    def copyTo_click(self):
        self.find_element(*self.copyTo_loc).click()


#添加抄送对象

    copyTo_employee_loc=(By.CLASS_NAME,"android.widget.LinearLayout")
    copyTo_department_loc=(By.ID,"com.uniubi.attendance:id/tv_cp_to_depart")
    copyTo_button_loc=(By.ID,"com.uniubi.attendance:id/bt_copy_to_enter")

    def copyTo_employee(self):
        self.find_elements(*self.copyTo_employee_loc)[0].click()
        sleep(1)
        self.find_element(*self.copyTo_department_loc).click()
        self.find_elements(*self.copyTo_employee_loc)[1].click()
        sleep(1)
        self.find_element(*self.copyTo_button_loc).click()

#点击审批
    approver_loc=(By.ID,"com.uniubi.attendance:id/tv_select_approver")
    def approver_click(self):
        self.find_element(*self.approver_loc).click()

#添加审批对象
    approver_employee_loc=(By.CLASS_NAME,"android.widget.LinearLayout")
    approver_department_loc=(By.ID,"com.uniubi.attendance:id/tv_choose_Department")
    approver_department_employee=(By.CLASS_NAME,"android.widget.RelativeLayout")
    approver_button_loc=(By.ID,"com.uniubi.attendance:id/bt_copy_to_enter")

    def approver_employee(self):
        self.find_element(*self.approver_department_loc).click()
        sleep(1)
        self.find_elements(*self.approver_department_employee)[0].click()
        self.find_elements(*self.approver_department_employee)[4].click()

#提交
    commit_loc=(By.ID,"com.uniubi.attendance:id/bt_leave_commit")
    def commit(self):
        self.find_element(*self.commit_loc).click()


#统一请假接口
    def leave(self,i,start_hour,start_minute,end_hour,end_minute,reason):
        sleep(5)
        self.process_click()
        #点击请假
        self.leave_click()
        self.Systemtime4()
        print(self.Systemtime4())
        #选请假类型
        self.process_type(i)
        #点击开始时间
        self.starttime_click()
        #选择开始时间
        self.choose_startTime(start_hour,start_minute)
        #点击结束时间
        self.leaveend_click()
        #选择结束时间
        self.choose_endTime(end_hour,end_minute)
        #备注
        self.reason_leave(reason)

        #选择抄送人
        self.copyTo_click()
        #添加抄送对象
        self.copyTo_employee()
        #选择审批人
        self.approver_click()
        #选择审批对象
        self.approver_employee()
        #提交
        self.commit()
        sleep(1)


#补签
    resigned_loc=(By.ID,"com.uniubi.attendance:id/ll_signed")
    resigned_start_time=(By.ID,"com.uniubi.attendance:id/ll_time")

    resign_reason=(By.ID,"com.uniubi.attendance:id/tv_fill_reason")
#点击补签
    def resigned_click(self):
        self.find_element(*self.resigned_loc).click()

    def resign_time_click(self):
        self.find_element(*self.resigned_start_time).click()
        sleep(1)

    def resigned_choose_time(self):
        start_time=(By.ID,"android:id/numberpicker_input")
        start_time_button=(By.ID,"android:id/button1")
        startTime_H = int(self.find_elements(*self.start_time)[1].text)
        startTime_M = int(self.find_elements(*self.start_time)[2].text)
    # 获取小时坐标
        x1 = int(self.getSize()[0] * 0.55)
        y1 = int(self.getSize()[1] * 0.45)
        y2 = int(self.getSize()[1] * 0.54)

    # 获取分钟坐标
        x1_M = int(self.getSize()[0] * 0.75)
        y1_M = int(self.getSize()[1] * 0.45)
        y2_M = int(self.getSize()[1] * 0.54)

        # 获取天坐标
        x1_D = int(self.getSize()[0] * 0.35)
        y1_D = int(self.getSize()[1] * 0.45)
        y2_D = int(self.getSize()[1] * 0.54)

        self.driver.swipe(x1, y1, x1, y2, 500)
        self.driver.swipe(x1_M, y1_M, x1_M, y2, 500)
        self.find_element(*self.start_time_button).click()





    def resigned_reson(self,reason):
        self.find_element(*self.resign_reason).click()
        sleep(1)
        self.find_element(*self.resign_reason).send_keys(reason)


    #补签提交
    resigned_commit_loc=(By.ID,"com.uniubi.attendance:id/bt_fill_commit")
    def resigned_commit(self):
        self.find_element(*self.resigned_commit_loc).click()

#定义统一补签接口
    def resigned(self,reason):
        sleep(5)
        self.process_click()
        #点击补签
        a=self.Systemtime2()
        print(a)
        self.resigned_click()
        # 获取系统时间
        #点击补签时间
        self.resign_time_click()
        # print(self.find_elements(*self.start_time)[1].text)
        # print(self.find_elements(*self.start_time)[2].text)


        #选择补签时间
        self.resigned_choose_time()
        #选择补签理由
        self.resigned_reson(reason)

        #点击抄送人
        self.copyTo_click()
        self.copyTo_employee()
        #点击审批人
        self.approver_click()
        self.approver_employee()
        self.resigned_commit()


#其他流程

    other_loc=(By.ID,"com.uniubi.attendance:id/ll_other")

    other_title_loc=(By.ID,"com.uniubi.attendance:id/atv_title")
    other_commit_loc=(By.ID,"com.uniubi.attendance:id/bt_other_commit")
    other_starttime_loc=(By.ID,"com.uniubi.attendance:id/ll_start_time")
    other_endtime_loc=(By.ID,"com.uniubi.attendance:id/rl_leave_end")
#点击其他流程
    def other_click(self):
        self.find_element(*self.other_loc).click()

#填写标题
    def other_title(self,title):
        self.find_element(*self.other_title_loc).click()
        self.find_element(*self.other_title_loc).send_keys(title)
#点击开始时间
    def other_starttime_click(self):
        self.find_element(*self.other_starttime_loc).click()


#选择开始时间

    def other_choose_starttime(self):
        start_time=(By.ID,"android:id/numberpicker_input")
        start_time_button=(By.ID,"android:id/button1")
        startTime_H = int(self.find_elements(*self.start_time)[1].text)
        startTime_M = int(self.find_elements(*self.start_time)[2].text)
    # 获取小时坐标
        x1 = int(self.getSize()[0] * 0.55)
        y1 = int(self.getSize()[1] * 0.45)
        y2 = int(self.getSize()[1] * 0.54)

    # 获取分钟坐标
        x1_M = int(self.getSize()[0] * 0.75)
        y1_M = int(self.getSize()[1] * 0.45)
        y2_M = int(self.getSize()[1] * 0.54)

        self.driver.swipe(x1, y1, x1, y2, 500)
        self.driver.swipe(x1_M, y1_M, x1_M, y2, 500)
        self.find_element(*self.start_time_button).click()
#点击结束时间
    def other_endtime_click(self):
        self.find_element(*self.other_endtime_loc).click()
#选择结束时间
    def other_choose_endtime(self):

        start_time=(By.ID,"android:id/numberpicker_input")
        start_time_button=(By.ID,"android:id/button1")
        startTime_H = int(self.find_elements(*self.start_time)[1].text)
        startTime_M = int(self.find_elements(*self.start_time)[2].text)
# 获取小时坐标
        x1 = int(self.getSize()[0] * 0.55)
        y1 = int(self.getSize()[1] * 0.45)
        y2 = int(self.getSize()[1] * 0.36)

# 获取分钟坐标
        x1_M = int(self.getSize()[0] * 0.75)
        y1_M = int(self.getSize()[1] * 0.45)
        y2_M = int(self.getSize()[1] * 0.36)

        self.driver.swipe(x1, y1, x1, y2, 500)
        self.driver.swipe(x1_M, y1_M, x1_M, y2, 500)
        self.find_element(*self.start_time_button).click()
#填写备注
    other_reason_loc = (By.ID, "com.uniubi.attendance:id/et_leave_reason")
    def other_reason(self,reason):
        self.find_element(*self.other_reason_loc).click()
        self.find_element(*self.other_reason_loc).send_keys(reason)

#提交
    def other_commit(self):
        self.find_element(*self.other_commit_loc).click()

#统一其他流程接口
    def other_withendtime(self,title,reason):
        sleep(5)
        #点击菜单栏的流程
        self.process_click()
        #点击其他流程
        self.other_click()
        #系统时间
        self.Systemtime1()
        #填写其他流程标题
        self.other_title(title)
        #点击开始时间
        self.other_starttime_click()
        print(self.find_elements(*self.start_time)[2].text)
        #选择开始时间
        self.other_choose_starttime()
        #点击结束时间
        self.other_endtime_click()
        #选择结束时间
        self.other_choose_endtime()

        #填写请假理由
        self.other_reason(reason)
        #点击抄送
        self.copyTo_click()
        self.copyTo_employee()
        #点击审批人
        self.approver_click()
        self.approver_employee()
        #提交
        self.other_commit()

    def other_withoutendtime(self,title,reason):
        sleep(5)
        #点击菜单栏的流程
        self.process_click()
        #点击其他流程
        self.other_click()
        #系统时间
        self.Systemtime1()
        #填写其他流程标题
        self.other_title(title)
        #点击开始时间
        self.other_starttime_click()
        #选择开始时间
        self.other_choose_starttime()

        #填写请假理由
        self.other_reason(reason)
        #点击抄送
        self.copyTo_click()
        self.copyTo_employee()
        #点击审批人
        self.approver_click()
        self.approver_employee()
        #提交
        self.other_commit()

#请出差假

    outwork_loc=(By.ID,"com.uniubi.attendance:id/ll_evection")
    outwork_starttime_loc=(By.ID,"com.uniubi.attendance:id/ll_out_work_start")
    outwork_endtime_loc=(By.ID,"com.uniubi.attendance:id/ll_out_work_end")
    outwork_reason_loc=(By.ID,"com.uniubi.attendance:id/et_out_work_reason")
    outwork_surebutton_loc=(By.CLASS_NAME,"android.widget.Button")
    outwork_commit_loc=(By.ID,"com.uniubi.attendance:id/bt_out_work_commit")

#点击出差
    def outwork_click(self):
        self.find_element(*self.outwork_loc).click()
#点击开始时间
    def outwork_choose_starttime(self):
        self.find_element(*self.outwork_starttime_loc).click()
        sleep(1)
        self.find_elements(*self.outwork_surebutton_loc)[1].click()

#点击结束时间
    def outwork_choose_endtime(self):
        self.find_element(*self.outwork_endtime_loc).click()
        sleep(1)
        self.find_elements(*self.outwork_surebutton_loc)[1].click()

#出差理由
    def outwork_reason(self,reason):
        self.find_element(*self.outwork_reason_loc).click()
        self.find_element(*self.outwork_reason_loc).send_keys(reason)
#提交出差申请
    def outwork_commit(self):
        self.find_element(*self.outwork_commit_loc).click()


#统一定义出差接口

    def outwork(self,reason):
        sleep(5)
        #点击流程
        self.process_click()
        #点击出差
        self.outwork_click()
        #选择开始时间
        self.outwork_choose_starttime()
        #选择结束时间
        self.outwork_choose_endtime()
        #出差理由
        self.outwork_reason(reason)
        #抄送人
        self.copyTo_click()
        self.copyTo_employee()
        #审批人
        self.approver_click()
        self.approver_employee()
        #提交
        self.outwork_commit()


    def outwork_choose_starttime_future(self):
        self.find_element(*self.outwork_starttime_loc).click()
    # 获取小时坐标
        x1 = int(self.getSize()[0] * 0.7)
        y1 = int(self.getSize()[1] * 0.82)
        y2 = int(self.getSize()[1] * 0.75)



        self.driver.swipe(x1, y1, x1, y2, 500)

        self.find_elements(*self.outwork_surebutton_loc)[1].click()

#统一未来出差接口

    def outwork_future(self,reason):
        sleep(10)
        #点击流程
        self.process_click()
        #点击出差
        self.outwork_click()
        a=self.Systemtime5()
        print("系统时间+1")
        print(a)

        #选择开始时间
        self.outwork_choose_starttime_future()
        #选择结束时间
        self.outwork_choose_endtime()
        #出差理由
        self.outwork_reason(reason)
        #抄送人
        self.copyTo_click()
        self.copyTo_employee()
        #审批人
        self.approver_click()
        self.approver_employee()
        #提交
        self.outwork_commit()