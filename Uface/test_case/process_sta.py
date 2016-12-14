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
from models.function import modifyTimeTpye


class processTest(myunit.MyTest):
    # 第一审批人
        approver_employee = "张波"
    # 第二审批人
        approver_employee2 = "包曙源"
    # 申请人
        applier = "1郑晓龙1"
    # 申请人账号
        email_applier1 = "18768172337"
        password_applier1 = "172337"
    # 第一审批人账号
        email_approver1 = "18868123457"
        password_approver1 = "123457"
    # 第二审批人账号
        email_approver2 = "18878123456"
        password_approver2 = "123456"
    # 当天时间
        Today0 = datetime.datetime.now()
        Y = Today0.strftime('%Y')
    # 把时间中出现的2位时间转换为1位  如09变9
        m = int(Today0.strftime('%m'))
        d = int(Today0.strftime('%d'))
        Today = str(Y) + "-" + str(m) + "-" + str(d)

        def test_process1(self):
            """开始"""
            print("小试牛刀")

        def test_process2(self):
            """请事假，10点到11点 申请人：1郑晓龙1，审批人：张波"""
            process(self.driver).leave(1, 10, 0, 11, 0, "请事假一小时，有事情")

        def test_process3(self):
            """请病假，11点到13点 申请人：1郑晓龙1，审批人：张波"""
            process(self.driver).leave(2, 11, 0, 13, 0, "请病假二小时，有事情")

        def test_process4(self):
            """请年假，13点到15点 申请人：1郑晓龙1，审批人：张波"""
            process(self.driver).leave(3, 13, 0, 15, 0, "请年假二小时，有事情")

        def test_process5(self):
            """请产假，13点到15点 申请人：1郑晓龙1，审批人：张波"""
            process(self.driver).leave(4, 15, 0, 16, 0, "请产假二小时，有事情")

        def test_process6(self):
            """请特殊假，16点到17点 申请人：1郑晓龙1，审批人：张波"""
            process(self.driver).leave(5, 16, 0, 17, 0, "请特殊假一小时，有事情")

        def test_process7(self):
            """补签 理由：打卡机损坏，申请人：1郑晓龙1，审批人：张波"""
            process(self.driver).resigned("打卡机损坏")

        def test_process8(self):
            """其他假(有结束时间) """
            process(self.driver).other_withendtime("陪客户吃饭", "杭州宇泛智能科技赵总来访")

        def test_process9(self):
            """其他假(无结束时间) """
            process(self.driver).other_withoutendtime("陪客户吃饭", "杭州宇泛智能科技赵总来访")


        def test_process10(self):
            """其他假（有结束时间）：点击申请中，查看详情并且进行撤销操作"""
            processResult(self.driver).processing_detail("其他申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "其他:陪客户吃饭")
            #其他申请的开始时
            Date1=process(self.driver).returnSystemtime1()-datetime.timedelta(hours=1)-datetime.timedelta(minutes=1)
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
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            #撤销其他申请
            processResult(self.driver).backout()
            print("其他申请有结束时间的流程通过")

        def test_process11(self):
            """其他假（无结束时间）：点击申请中，查看详情并且进行撤销操作"""
            process(self.driver).other_withoutendtime("陪客户吃饭", "杭州宇泛智能科技赵总来访")
            processResult(self.driver).processing_detail("其他申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "其他:陪客户吃饭")
            #其他申请的开始时

            print(process(self.driver).returnSystemtime1())
            Date1=process(self.driver).returnSystemtime1()-datetime.timedelta(hours=1)-datetime.timedelta(minutes=1)
            time1=Date1.strftime('%Y')
            #把时间中出现的2位时间转换为1位  如09变9
            time1_m=int(Date1.strftime('%m'))
            time1_d=int(Date1.strftime('%d'))
            time1_H=Date1.strftime('%H:%M')
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),(time1+"-"+str(time1_m)+"-"+str(time1_d)+"  "+time1_H))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),"无")
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(),"杭州宇泛智能科技赵总来访")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            #撤销其他申请
            processResult(self.driver).backout()
            print("其他申请无结束时间的流程通过")

        def test_process12(self):
            """补签流程：点击申请中，查看详情并且进行撤销操作"""
            process(self.driver).resigned("打卡机损坏")
            processResult(self.driver).processing_detail("补签申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "补签")
            # 补签申请
            print(process(self.driver).returnSystemtime2())
            Date1 = process(self.driver).returnSystemtime2() - datetime.timedelta(hours=1) - datetime.timedelta(minutes=1)
            time1 = Date1.strftime('%Y')
            # 把时间中出现的2位时间转换为1位  如09变9
            time1_m = int(Date1.strftime('%m'))
            time1_d = int(Date1.strftime('%d'))
            time1_H = Date1.strftime('%H:%M')
             # 补签时间保存
              #第一次申请补签的时间
            resign_time1 = time1 + "-" + str(time1_m) + "-" + str(time1_d) + "  " + time1_H
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),(time1 + "-" + str(time1_m) + "-" + str(time1_d) + "  " + time1_H))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "打卡机损坏")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            # 撤销补签申请
            processResult(self.driver).backout()
            print("补签流程测试通过")

        def test_process13(self):
            """出差流程：点击申请中，查看详情并且进行撤销操作"""
            process(self.driver).outwork_future("上海出差一整天")
            processResult(self.driver).processing_detail("出差申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "出差")
            Date1 = process(self.driver).returnSystemtime5()
            Date1=Date1.strftime('%Y-%m-%d')
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             Date1)
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             Date1)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "上海出差一整天")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).backout()
            print("出差流程测试通过")

        def test_process14(self):
            """请假流程（特殊假）：点击申请中，查看详情并且进行撤销操作"""
            process(self.driver).leave(5, 16, 0, 17, 0, "请特殊假一小时，有事情")

            processResult(self.driver).processing_detail("特殊假申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:特殊假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today+"  16:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today+"  17:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请特殊假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).backout()
            print("特殊假流程测试通过")

        def test_process15(self):
            """请假流程（产假）：点击申请中，查看详情并且进行撤销操作"""
            process(self.driver).leave(4, 15, 0, 16, 0, "请产假二小时，有事情")
            processResult(self.driver).processing_detail("产假申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:产假")

            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today  +"  15:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today  +"  16:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请产假二小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).backout()
            print("产假流程测试通过")

        def test_process16(self):
            """请假流程（年假）：点击申请中，查看详情并且进行撤销操作"""
            process(self.driver).leave(3, 13, 0, 15, 0, "请年假二小时，有事情")
            processResult(self.driver).processing_detail("年假申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:年假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today  +"  13:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today  +"  15:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请年假二小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).backout()
            print("年假流程测试通过")

        def test_process17(self):
            """请假流程（病假）：点击申请中，查看详情并且进行撤销操作"""

            process(self.driver).leave(2, 11, 0, 13, 0, "请病假二小时，有事情")
            processResult(self.driver).processing_detail("病假申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:病假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today+"  11:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today+"  13:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请病假二小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).backout()
            print("病假流程测试通过")

        def test_process18(self):
            """请假流程（事假）：点击申请中，查看详情并且进行撤销操作"""

            process(self.driver).leave(1, 10, 0, 11, 0, "请事假一小时，有事情")  # 请事假，10点到11点
            processResult(self.driver).processing_detail("事假申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:事假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today+"  10:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today+"  11:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请事假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).backout()
            print("事假流程测试通过")


        outwork_futuretime1=datetime.datetime.now()


        def test_process19(self):
            """审批出差（无第二审批人）--拒绝：申请出差，切换账号，审批-拒绝"""

            process(self.driver).outwork_future("明天上海出差一整天")
            global outwork_futuretime1
            outwork_futuretime1= process(self.driver).returnSystemtime5()
            outwork_futuretime1=outwork_futuretime1.strftime('%Y-%m-%d')
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approving(processTest().applier, "补签")
            self.assertEqual(processResult(self.river).processing_detailInfo_title(), "出差")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),outwork_futuretime1)
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),outwork_futuretime1)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "明天上海出差一整天")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).approving_detail1("复议","拒绝")
            #切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)


        def test_process20(self):
            """查看已拒绝中的出差：对比已通过中的出差详情"""
            processResult(self.driver).failed("出差申请")
            self.assertEqual(processResult(self.river).processing_detailInfo_title(), "出差")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),outwork_futuretime1)
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),outwork_futuretime1)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "明天上海出差一整天")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)

        def test_process21(self):
            """查看已审批中的出差：且对比详情数据"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approved(processTest().applier, "出差")
            self.assertEqual(processResult(self.river).approved_detailInfo_title(), "出差")
            self.assertEqual(processResult(self.driver).approved_detailInfo_starttime(), outwork_futuretime1)
            self.assertEqual(processResult(self.driver).approved_detailInfo_endtime(), outwork_futuretime1)
            self.assertEqual(processResult(self.driver).approved_detailInfo_reason(), "明天上海出差一整天")
            self.assertEqual(processResult(self.driver).approved_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).approved_detailInfo_status1(), "已拒绝")
            self.assertEqual(processResult(self.driver).approved_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).approved_detailInfo_name1(), processTest().approver_employee)
            #切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)


        outwork_futuretime2 = datetime.datetime.now()
        def test_process22(self):
            """审批出差（有第二审批人）--第一审批人通过：申请出差，切换账号，审批-通过。第二审批人通过：切换账号，审批-通过"""
            process(self.driver).outwork_future("明天上海出差一整天")
            global outwork_futuretime2
            outwork_futuretime2= process(self.driver).returnSystemtime5()
            outwork_futuretime2=outwork_futuretime2.strftime('%Y-%m-%d')
            #切换第一审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approving( processTest().applier,"出差")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "出差")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),outwork_futuretime2)
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),outwork_futuretime2)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "明天上海出差一整天")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).approving_detail1("辛苦", "通过")
            #第二审批人
            # 切换第二审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver2, processTest().password_approver2)
            processResult(self.driver).approving( processTest().applier, "出差")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "出差")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),outwork_futuretime2)
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),outwork_futuretime2)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "明天上海出差一整天")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            processResult(self.driver).approving_detail2("辛苦", "通过")
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)


        def test_process23(self):
            """查看已通过中的出差申请：对比已通过中的出差详情"""
            processResult(self.driver).passed("出差申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "出差")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),outwork_futuretime2)
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),outwork_futuretime2)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "明天上海出差一整天")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)

        def test_process24(self):
            """查看已审批中的出差申请：对比已审批中的出差详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approved(processTest().applier, "出差")
            self.assertEqual(processResult(self.driver).approved_detailInfo_title(), "出差")
            self.assertEqual(processResult(self.driver).approved_detailInfo_starttime(),outwork_futuretime2)
            self.assertEqual(processResult(self.driver).approved_detailInfo_endtime(),outwork_futuretime2)
            self.assertEqual(processResult(self.driver).approved_detailInfo_reason(), "明天上海出差一整天")
            self.assertEqual(processResult(self.driver).approved_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).approved_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).approved_detailInfo_status2(), "已通过")
            self.assertEqual(processResult(self.driver).approved_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).approved_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).approved_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            #切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)


        resign_time1=datetime.datetime.now()
        def test_process25(self):
            """审批补签（无第二审批人）--拒绝：申请补签，切换账号，审批-拒绝"""
            process(self.driver).resigned("打卡机损坏1")
            global resign_time1
            resign_time1= process(self.driver).returnSystemtime2() - datetime.timedelta(hours=1) - datetime.timedelta( minutes=1)
            resign_time1=modifyTimeTpye(resign_time1)
            # 切换到第一审批账号登入
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            # 审批补签申请-拒绝
            processResult(self.driver).approving(processTest().applier, "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), resign_time1)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "打卡机损坏1")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).approving_detail1("拒绝", "拒绝")
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process26(self):
            """查看已拒绝中的补签申请：对比已通过中的补签详情"""
            processResult(self.driver).failed("补签申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), resign_time1)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "打卡机损坏1")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)

        def test_process27(self):
            """查看已审批中的补签申请：对比已审批中的补签详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approved(processTest().applier, "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), resign_time1)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "打卡机损坏1")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)



        resign_time2=datetime.datetime.now()

        def test_process28(self):
            """"审批补签（有第二审批人）--第一申请人通过：申请补签，切换账号，审批-通过。第二申请人;切换账号，审批-通过"""
            # 审批补签申请-通过--（复议-通过--有第二审批人--通过）
            process(self.driver).resigned("打卡机损坏2")
            global resign_time2
            resign_time2= process(self.driver).returnSystemtime2() - datetime.timedelta(hours=1) - datetime.timedelta(
                minutes=1)
            resign_time2 = modifyTimeTpye(resign_time2)
            # 切换到第一审批账号登入
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approving(processTest().applier, "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), resign_time2)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "打卡机损坏2")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).approving_detail1("复议", "通过")
            # 切换第二审批人账号登入
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver2, processTest().password_approver2)
            processResult(self.driver).approving(processTest().applier, "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), resign_time2)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "打卡机损坏2")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            processResult(self.driver).approving_detail2("辛苦", "通过")
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process29(self):
            """查看已通过中的补签申请：对比已通过中的补签详情"""
            processResult(self.driver).passed("补签申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), resign_time2)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "打卡机损坏2")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)

        def test_process30(self):
            """查看已审批中的补签申请：对比已审批中的补签详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approved(processTest().applier, "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), resign_time2)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "打卡机损坏2")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)


        resign_time3=datetime.datetime.now()
        def test_process31(self):
            """"审批补签（有第二审批人）--第一申请人通过：申请补签，切换账号，审批-通过。第二申请人;切换账号，审批-拒绝"""
            # 审批补签申请-通过----第二审批人--拒绝）
            process(self.driver).resigned("打卡机损坏3")
            global resign_time3
            resign_time3= process(self.driver).returnSystemtime2() - datetime.timedelta(hours=1) - datetime.timedelta( minutes=1)
            resign_time3=modifyTimeTpye(resign_time3)
            # 切换到第一审批账号登入
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approving(processTest().applier, "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), resign_time3)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "打卡机损坏3")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).approving_detail1("理由不充分", "通过")
            # 换第二审批人账号登入
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver2, processTest().password_approver2)
            processResult(self.driver).approving(processTest().applier, "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), resign_time3)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "打卡机损坏3")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)

            processResult(self.driver).approving_detail2("辛苦", "拒绝")
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process32(self):
            """查看已拒绝中的补签申请（有第二审批人）：对比已拒绝中的补签详情"""
            processResult(self.driver).failed("补签申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), resign_time3)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "打卡机损坏2")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)

        def test_process33(self):
            """查看已审批中的补签申请（有第二审批人）：对比第一审批人中的的补签详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approved(processTest().applier, "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), resign_time3)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "打卡机损坏2")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process34(self):
            """查看已审批中的补签申请（有第二审批人）：对比第二审批人中的的补签详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver2, processTest().password_approver2)
            processResult(self.driver).approved(processTest().applier, "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "补签")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), resign_time3)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "打卡机损坏2")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process35(self):
            """"审批特殊假--拒绝（无第二审批人）--第一申请人拒绝：申请特殊假，切换账号，审批-拒绝。"""
            process(self.driver).leave(5, 16, 0, 17, 0, "请特殊假一小时，有事情")  # 请特殊假，16点到17点
            # 切换到第一审批账号登入
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approving( processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:特殊假")
            self.assertEprocessResult(self.driver).approving( processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), (processTest().Today+"  16:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(), (processTest().Today+"  17:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请特殊假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).approving_detail1("复议", "拒绝")
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process36(self):
            """查看已拒绝中的特殊假申请：对比已拒绝中的特殊假详情"""
            processResult(self.driver).failed("特殊假申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "特殊假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  16:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  17:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请特殊假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)

        def test_process37(self):
            """查看已审批中的特殊假申请：对比已审批中的特殊假详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approved(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "特殊假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  16:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  17:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请特殊假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)


        def test_process38(self):
            """"审批特殊假--拒绝（有第二审批人）--第一审批人通过：申请特殊假，切换账号，审批-通过。第二审批人：切换账号，审批-拒绝"""
            process(self.driver).leave(5, 16, 0, 17, 0, "请特殊假一小时，有事情")  # 请特殊假，16点到17点
            # 切换第一审批人账号登入
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approving(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:特殊假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  16:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  17:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请特殊假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).approving_detail1("同意", "通过")
            # 换账第二申请人账号登入
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver2, processTest().password_approver2)
            processResult(self.driver).approving(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:特殊假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  16:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  17:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请特殊假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            processResult(self.driver).approving_detail2("拒绝", "拒绝")
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)


        def test_process39(self):
            """查看已拒绝中的特殊假申请（有第二审批人）：对比已拒绝中的特殊假详情"""
            processResult(self.driver).failed("特殊假申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:特殊假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  16:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  17:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请特殊假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)

        def test_process40(self):
            """查看已审批中的特殊假申请（有第二审批人）：对比第一审批人中的特殊假详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approved(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:特殊假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  16:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  17:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请特殊假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process41(self):
            """查看已审批中的特殊假申请（有第二审批人）：对比第二审批人中的特殊假详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver2, processTest().password_approver2)
            processResult(self.driver).approved(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:特殊假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  16:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  17:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请特殊假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process42(self):
            """"审批产假--拒绝（无第二审批人）--第一审批人拒绝：申请产假，切换账号，审批-拒绝。"""
            process(self.driver).leave(4, 15, 0, 16, 0, "请产假一小时，有事情")
            # 切换第一审批人账号登入
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approving( processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:产假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), (processTest().Today+"  15:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(), (processTest().Today+"  16:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请产假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).approving_detail2("复议", "拒绝")
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process43(self):
            """查看已拒绝中的产假申请：对比已拒绝中的产假详情"""
            processResult(self.driver).failed("产假申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:产假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), (processTest().Today+"  15:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(), (processTest().Today+"  16:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请产假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)

        def test_process44(self):
            """查看已审批中的产假申请：对比已审批中的产假详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approved(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:产假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), (processTest().Today+"  15:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(), (processTest().Today+"  16:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请产假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process45(self):
            """"审批产假--通过（有第二审批人）--第一审批人通过：申请产假，切换账号，审批-通过。第二审批人：切换账号，审批-通过"""
            process(self.driver).leave(4, 15, 0, 16, 0, "请产假一小时，有事情")
            # 切换第一审批人账号登入
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approving( processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:产假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), (processTest().Today+"  15:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(), (processTest().Today+"  16:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请产假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).approving_detail1("同意", "通过")
            #换账号登入
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver2,processTest().password_approver2)
            processResult(self.driver).approving( processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:产假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),(processTest().Today+"  15:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),(processTest().Today+"  16:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请产假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            processResult(self.driver).approving_detail2("辛苦", "通过")
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process46(self):
            """查看已通过中的产假申请（有第二审批人）：对比已通过中的产假详情"""
            processResult(self.driver).passed("产假申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:产假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  15:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  16:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请产假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)

        def test_process47(self):
            """查看已审批中的产假申请（有第二审批人）：对比第一审批人中的产假详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approved(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:产假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  15:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  16:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请产假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process48(self):
            """查看已审批中的产假申请（有第二审批人）：对比第二审批人中的产假详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver2, processTest().password_approver2)
            processResult(self.driver).approved(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:产假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  15:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  16:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请产假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)


        def test_process49(self):
            """"审批年假--拒绝（无第二审批人）--第一审批人拒绝：申请年假，切换账号，审批-拒绝。"""
            process(self.driver).leave(3, 13, 0, 15, 0, "请年假二小时，有事情")  # 请年假，13点到15点
            # 切换第一审批人账号登入
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approving( processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:年假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), (processTest().Today+"  13:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(), (processTest().Today+"  15:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请年假二小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).approving_detail2("复议", "拒绝")
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process50(self):
            """查看已拒绝中的年假申请：对比已拒绝中的年假详情"""
            processResult(self.driver).failed("年假申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:年假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  13:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  15:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请年假二小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)

        def test_process51(self):
            """查看已审批中的年假申请：对比已审批中的年假详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approved(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:年假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  13:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  15:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请年假二小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process52(self):
            """"审批年假--通过（有第二审批人）--第一审批人通过：申请年假，切换账号，审批-通过。第二审批人：切换账号，审批-通过"""
            process(self.driver).leave(3, 13, 0, 15, 0, "请年假二小时，有事情")  # 请年假，13点到15点
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approving(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:年假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  13:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  15:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请年假二小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).approving_detail1("同意", "通过")
            # 换第二审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver2, processTest().password_approver2)
            processResult(self.driver).approving(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:年假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  13:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  15:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请年假二小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            processResult(self.driver).approving_detail2("辛苦", "通过")
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process53(self):
            """查看已通过中的年假申请（有第二审批人）：对比已通过中的年假详情"""
            processResult(self.driver).passed("年假申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:年假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  13:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  15:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请年假二小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)

        def test_process54(self):
            """查看已审批中的年假申请（有第二审批人）：对比第一审批人中的年假详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approved(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:年假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  13:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  15:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请年假二小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process55(self):
            """查看已审批中的年假申请（有第二审批人）：对比第二审批人中的年假详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver2, processTest().password_approver2)
            processResult(self.driver).approved(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:年假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  13:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  15:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请年假二小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process56(self):
            """"审批病假--拒绝（无第二审批人）--第一审批人拒绝：申请病假，切换账号，审批-拒绝。"""
            process(self.driver).leave(2, 11, 0, 13, 0, "请病假二小时，有事情")  # 请病假，11点到13点
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approving( processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:病假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), (processTest().Today+"  11:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(), (processTest().Today+"  13:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请年假二小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).approving_detail1("复议", "拒绝")
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process57(self):
            """查看已拒绝中的病假申请：对比已拒绝中的病假详情"""
            processResult(self.driver).failed("病假申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:病假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  11:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  13:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请年假二小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)

        def test_process58(self):
            """查看已审批中的病假申请：对比已审批中的病假详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approved(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:病假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  11:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  13:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请年假二小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process59(self):
            """"审批病假--通过（无第二审批人）--第一审批人通过：申请病假，切换账号，审批-通过"""
            process(self.driver).leave(2, 11, 0, 13, 0, "请病假二小时，有事情")  # 请病假，11点到13点
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approving( processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:病假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), (processTest().Today+"  11:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(), (processTest().Today+"  13:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请病假二小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).approving_detail2("辛苦", "通过")
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process60(self):
            """查看已通过中的病假申请：对比已通过中的病假详情"""
            processResult(self.driver).passed("病假申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:病假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  11:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  13:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请年假二小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)


        def test_process61(self):
            """查看已审批中的病假申请：对比已审批中的病假详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approved(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:病假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  11:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  13:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请年假二小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process62(self):
            """"审批事假--拒绝（无第二审批人）--第一审批人拒绝：申请事假，切换账号，审批-拒绝。"""
            process(self.driver).leave(1, 10, 0, 11, 0, "请事假一小时，有事情")  # 请事假，10点到11点
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approving( processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:事假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),(processTest().Today+"  10:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),(processTest().Today+"  11:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请事假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).approving_detail1("理由不充分", "拒绝")
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)


        def test_process63(self):
            """查看已拒绝中的事假申请：对比已拒绝中的事假详情"""
            processResult(self.driver).failed("事假申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:事假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  10:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  11:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请事假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)

        def test_process64(self):
            """查看已审批中的事假申请：对比已审批中的事假详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approved(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:事假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  10:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  11:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请事假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已拒绝")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)


        def test_process65(self):
            """"审批事假--通过（无第二审批人）--第一审批人通过：申请事假，切换账号，审批-通过"""
            process(self.driver).leave(1, 10, 0, 11, 0, "请事假一小时，有事情")  # 请事假，10点到11点
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approving( processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:事假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), (processTest().Today+"  10:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(), (processTest().Today+"  11:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请事假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).approving_detail2("同意", "通过")
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process66(self):
            """查看已通过中的事假申请：对比已通过中的事假详情"""
            processResult(self.driver).passed("事假申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:事假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  10:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  11:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请事假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)

        def test_process67(self):
            """查看已审批中的事假申请：对比已审批中的事假详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approved(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "请假:事假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),
                             (processTest().Today + "  10:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),
                             (processTest().Today + "  11:00"))
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "请事假一小时，有事情")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)


        other_starttime1=datetime.datetime.now()
        other_endtime1=datetime.datetime.now()
        def test_process68(self):
            """"审批其他假--拒绝（无第二审批人）--第一审批人通过：申请其他假，切换账号，审批-拒绝"""
            process(self.driver).other_withendtime("陪客户吃饭","杭州宇泛智能科技赵总来访")
            global other_starttime1
            other_starttime1=process(self.driver).returnSystemtime1()-datetime.timedelta(hours=1)-datetime.timedelta(minutes=1)
            global other_endtime1
            other_endtime1=process(self.driver).returnSystemtime1()
            other_starttime1 = modifyTimeTpye(other_starttime1)
            other_endtime1 = modifyTimeTpye(other_endtime1)
            # 切换第一审批人账号登入
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approving( processTest().applier, "其他")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "其他:陪客户吃饭")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(),other_starttime1)
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(),other_endtime1)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "杭州宇泛智能科技赵总来访")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(),  processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).approving_detail1("理由不充分","拒绝")
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process69(self):
            """查看已拒绝中的其他假申请：对比已拒绝中的其他假详情"""
            processResult(self.driver).failed("事假申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "其他:陪客户吃饭")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), other_starttime1)
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(), other_endtime1)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "杭州宇泛智能科技赵总来访")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)

        def test_process70(self):
            """查看已审批中的其他假申请：对比已审批中的其他假详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approved(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "其他:陪客户吃饭")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), other_starttime1)
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(), other_endtime1)
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "杭州宇泛智能科技赵总来访")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)


        other_starttime2=datetime.datetime.now()
        def test_process71(self):
            """"审批其他假--通过（有第二审批人）--第一审批人通过：申请其他假，切换账号，审批-通过。第二审批人：切换账号，审批-通过"""
            process(self.driver).other_withoutendtime("陪客户吃饭", "杭州宇泛智能科技赵总来访")
            global other_starttime2
            other_starttime2=process(self.driver).returnSystemtime1()-datetime.timedelta(hours=1)-datetime.timedelta(minutes=1)
            other_endtime2=process(self.driver).returnSystemtime1()
            other_starttime2 = modifyTimeTpye(other_starttime2)
            other_endtime2 = modifyTimeTpye(other_endtime2)
            # 切换第一审批人账号登入
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approving(processTest().applier, "其他")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "其他:陪客户吃饭")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), other_starttime2)
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(), "无")
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "杭州宇泛智能科技赵总来访")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            processResult(self.driver).approving_detail1("辛苦", "通过")
            # 换第二审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver2, processTest().password_approver2)
            processResult(self.driver).approving(processTest().applier, "其他")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "其他:陪客户吃饭")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), other_starttime2)
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(), "无")
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "杭州宇泛智能科技赵总来访")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            processResult(self.driver).approving_detail2("辛苦", "通过")
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process72(self):
            """查看已通过中的其他假申请：对比已通过中的其他假详情"""
            processResult(self.driver).passed("事假申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "其他:陪客户吃饭")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), other_starttime2)
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(), "无")
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "杭州宇泛智能科技赵总来访")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)

        def test_process73(self):
            """查看已审批中的其他假申请：对比第一审批人中的其他假详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver1, processTest().password_approver1)
            processResult(self.driver).approved(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "其他:陪客户吃饭")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), other_starttime2)
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(), "无")
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "杭州宇泛智能科技赵总来访")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)

        def test_process74(self):
            """查看已审批中的其他假申请：对比第二审批人中的其他假详情"""
            #切换审批人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_approver2, processTest().password_approver2)
            processResult(self.driver).approved(processTest().applier, "请假")
            self.assertEqual(processResult(self.driver).processing_detailInfo_title(), "其他:陪客户吃饭")
            self.assertEqual(processResult(self.driver).processing_detailInfo_starttime(), other_starttime2)
            self.assertEqual(processResult(self.driver).processing_detailInfo_endtime(), "无")
            self.assertEqual(processResult(self.driver).processing_detailInfo_reason(), "杭州宇泛智能科技赵总来访")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status0(), "发起申请")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status1(), "已通过")
            self.assertEqual(processResult(self.driver).processing_detailInfo_status2(), "审批中")
            self.assertEqual(processResult(self.driver).processing_detailInfo_name0(), processTest().applier)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name1(), processTest().approver_employee)
            self.assertEqual(processResult(self.driver).processing_detailInfo_name2(), processTest().approver_employee2)
            self.driver.keyenvet(4)
            self.driver.keyenvet(4)
            # 切换申请人账号
            login(self.driver).logoff()
            login(self.driver).login(processTest().email_applier1, processTest().password_applier1)



if __name__=="__main__":
    unittest.main()