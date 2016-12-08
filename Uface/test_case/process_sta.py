import unittest,sys;
sys.path.append("C:\\Users\\uni-ubi\\PycharmProjects\\Android_app\\Uface\\test_case")
from models import myunit
from page_obj.processPage import process
from page_obj.loginPage import login
from page_obj.previousInstall import install
from page_obj.processResultPage import processResult
from time import sleep
import time
import datetime



class processTest(myunit.MyTest):
        def test_process1(self):
            """所有流程"""
            # process(self.driver).leave(1,10,0,11,0,"请假一小时，有事情") #请事假，10点到11点
            #
            # process(self.driver).leave(2, 11, 0, 13, 0, "请假二小时，有事情")  # 请病假，11点到13点r
            #
            # process(self.driver).leave(3, 13, 0, 15, 0, "请假二小时，有事情")  # 请年假，13点到15点
            #
            # process(self.driver).leave(4, 15, 0, 16, 0, "请假二小时，有事情")  # 请产假，15点到16点
            #
            # process(self.driver).leave(5, 16, 0, 17, 0, "请假一小时，有事情")  # 请特殊假，16点到17点
            # #补签
            # process(self.driver).resigned("打卡机损坏")
            # #其他假
            # process(self.driver).other_withendtime("陪客户吃饭","杭州宇泛智能科技赵总来访")
            # process(self.driver).other_withoutendtime("陪客户吃饭", "杭州宇泛智能科技赵总来访")
            #申请中详情
            processResult(self.driver).processing_detail("其他申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "其他:陪客户吃饭")
            #其他申请的开始时间
            # print("请假开始时间全局变量返回")
            # print(process(self.driver).time_other)
            # print("请假开始时间全局变量方法返回")
            print(process(self.driver).returnSystemtime1())
            Date1=process(self.driver).returnSystemtime1()-datetime.timedelta(hours=1)-datetime.timedelta(minutes=1)
            # print("请假开始时间")
            # print(Date1)
            #其他申请的结束时间
            Date2 = process(self.driver).returnSystemtime1()
            time1=Date1.strftime('%Y')
            #把时间中出现的2位时间转换为1位  如09变9
            time1_m=int(Date1.strftime('%m'))
            time1_d=int(Date1.strftime('%d'))
            time1_H=Date1.strftime('%H:%M')
            time2=Date2.strftime('%Y')
            time2_m=int(Date2.strftime('%m'))
            time2_d=int(Date2.strftime('%d'))
            time2_H=Date2.strftime('%H:%M')

            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),(time1+"-"+str(time1_m)+"-"+str(time1_d)+"  "+time1_H))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),(time2+"-"+str(time2_m)+"-"+str(time2_d)+"  "+time2_H))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(),"杭州宇泛智能科技赵总来访")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), "1郑晓龙1")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), "徐宇杰")
            #撤销其他申请
            processResult(self.driver).backout()



        # def test_process2(self):
        #     """补签流程"""
        #     process(self.driver).resigned("打卡机损坏")

        # def test_process3(self):
        #     """其他流程"""
        #     #install(self.driver).install_ManagerforUnicode()#安装ManagerforUnicode
        #     process(self.driver).other_withendtime("陪客户吃饭","杭州宇泛智能科技赵总来访")
        #     process(self.driver).other_withoutendtime("陪客户吃饭", "杭州宇泛智能科技赵总来访")
        #
        # def test_process4(self):
        #     """出差申请"""
        #     process(self.driver).outwork("上海出差一整天")

        # def test_process5(self):
        #     """撤销流程"""
        #
            # processResult(self.driver).processing_detail("其他申请")
            # processResult(self.driver).breakout()


        # def test_process6(self):
        #     """已通过"""
        #     sleep(5)
        #     processResult(self.driver).process_click()
        #     processResult(self.driver).passed_click()
        #     processResult(self.driver).passed_detail_click("年假申请")
        #     self.assertEqual(processResult(self.driver).passed_detialInfo_title(),"请假:年假")
        #
        # def test_process7(self):
        #     """已拒绝"""
        #     sleep(5)
        #     processResult(self.driver).process_click()
        #     processResult(self.driver).passed_click()
        #     processResult(self.driver).failed_detail_click("年假申请")
        #     self.assertEqual(processResult(self.driver).failed_detialInfo_title(),"请假:年假")
        #
        # def test_process8(self):
        #     """需要我审批：有第二审批人"""
        #     processResult(self.driver).approving("金珍图","请假")
        #     self.assertEqual(processResult(self.driver).approving_detialInfo_title(),"请假:事假")
        #     # self.assertEqual(processResult(self.driver).approving_detialInfo_starttime(), "")
        #     # self.assertEqual(processResult(self.driver).approving_detialInfo_endtime(), "")
        #     # self.assertEqual(processResult(self.driver).approving_detialInfo_reason(), "")
        #     self.assertEqual(processResult(self.driver).approving_detialInfo_name0(), "金珍图")
        #     # self.assertEqual(processResult(self.driver).approving_detialInfo_name1(), "")
        #     # self.assertEqual(processResult(self.driver).approving_detialInfo_status0(), "")
        #     # self.assertEqual(processResult(self.driver).approving_detialInfo_status1(), "")
        #     processResult(self.driver).approving_detail1("同意","拒绝")
        #     #点击否
        #     processResult(self.driver).approving_notbutton_click()
        #     processResult(self.driver).approving_detail1("辛苦", "通过")
        #     processResult(self.driver).approving_surebutton_click()














if __name__=="__main__":
    unittest.main()