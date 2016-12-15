from email.mime.multipart import MIMEMultipart

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import time
import unittest
import os
import  sys
sys.path.append('C:\\Users\\uni-ubi\\PycharmProjects\\Android_app\\Uface\\test_case')

import login_sta
from process_sta import processTest




#==========定义发送邮件=========
def send_mail(new_file):
    print(new_file)
    f = open(new_file,"rb")
    mail_body = f.read()
    f.close()

    msg =MIMEText(mail_body,"html","utf-8")
    # msg["Content-Type"]='application/octet-stream'
    # msg["Content-Disposition"]='attachment,filename="uni-ubi.html"'
    # msgRoot=MIMEMultipart('related')
    # subject="登录界面自动化测试报告"
    # msg["Subject"]=subject
    msg["Subject"]=Header("登录界面自动化测试报告","utf-8")
    # msgRoot.attach(msg)
    msg['From'] = "自动化<qq741562314@126.com>"
    msg['To'] = "741562314@qq.com"

    smtp=smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.starttls()
    print("126邮箱登入前")
    smtp.login("qq741562314@126.com","a115211")
    print("126邮箱登入成功")
    smtp.sendmail("qq741562314@126.com","741562314@qq.com",msg.as_string())
    print("126发送邮件成功")
    smtp.quit()
    print("mail has send out")



#=====================查找测试报告目录，找到最新生产的测试报告文件====================
def new_report(testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getatime(testreport + "\\" +fn))
    file_new=os.path.join(testreport,lists[-1])
    print(testreport)
    print(file_new)
    return file_new

if __name__=="__main__":
    now= time.strftime("%Y-%m-%d %H_%M_%S")
    file_name="./report/" + now + "result.html"
    fp= open(file_name,"wb")
    runner =HTMLTestRunner(stream=fp,title="UniUbi登入测试报告",description="环境：W8，浏览器：firefox")
    # discover=unittest.defaultTestLoader.discover("./test_case/",pattern="*_sta.py")
    #
    # runner.run(discover)
    #单个测试用例运行
    suite= unittest.TestSuite()
    # suite.addTest(processTest("test_process1"))
    # suite.addTest(processTest("test_process2"))
    # suite.addTest(processTest("test_process3"))
    # suite.addTest(processTest("test_process4"))
    # suite.addTest(processTest("test_process5"))
    # suite.addTest(processTest("test_process6"))
    # suite.addTest(processTest("test_process7"))
    # suite.addTest(processTest("test_process8"))
    # suite.addTest(processTest("test_process9"))
    # suite.addTest(processTest("test_process10"))
    # suite.addTest(processTest("test_process11"))
    # suite.addTest(processTest("test_process12"))
    # suite.addTest(processTest("test_process13"))
    # suite.addTest(processTest("test_process14"))
    # suite.addTest(processTest("test_process15"))
    # suite.addTest(processTest("test_process16"))
    # suite.addTest(processTest("test_process17"))
    # suite.addTest(processTest("test_process18"))
    suite.addTest(processTest("test_process19"))
    suite.addTest(processTest("test_process20"))
    suite.addTest(processTest("test_process21"))
    suite.addTest(processTest("test_process22"))
    suite.addTest(processTest("test_process23"))
    suite.addTest(processTest("test_process24"))
    # suite.addTest(processTest("test_process25"))
    # suite.addTest(processTest("test_process26"))
    # suite.addTest(processTest("test_process27"))
    # suite.addTest(processTest("test_process28"))
    # suite.addTest(processTest("test_process29"))
    # suite.addTest(processTest("test_process30"))
    # suite.addTest(processTest("test_process31"))
    # suite.addTest(processTest("test_process32"))
    # suite.addTest(processTest("test_process33"))
    # suite.addTest(processTest("test_process34"))
    # suite.addTest(processTest("test_process35"))
    # suite.addTest(processTest("test_process36"))
    # suite.addTest(processTest("test_process37"))
    # suite.addTest(processTest("test_process38"))
    # suite.addTest(processTest("test_process39"))
    # suite.addTest(processTest("test_process40"))
    # suite.addTest(processTest("test_process41"))
    # suite.addTest(processTest("test_process42"))
    # suite.addTest(processTest("test_process43"))
    # suite.addTest(processTest("test_process44"))
    # suite.addTest(processTest("test_process45"))
    # suite.addTest(processTest("test_process46"))
    # suite.addTest(processTest("test_process47"))
    # suite.addTest(processTest("test_process48"))
    # suite.addTest(processTest("test_process49"))
    # suite.addTest(processTest("test_process50"))
    # suite.addTest(processTest("test_process51"))
    # suite.addTest(processTest("test_process52"))
    # suite.addTest(processTest("test_process53"))
    # suite.addTest(processTest("test_process54"))
    # suite.addTest(processTest("test_process55"))
    # suite.addTest(processTest("test_process56"))
    # suite.addTest(processTest("test_process57"))
    # suite.addTest(processTest("test_process58"))
    # suite.addTest(processTest("test_process59"))
    # suite.addTest(processTest("test_process60"))
    # suite.addTest(processTest("test_process61"))
    # suite.addTest(processTest("test_process62"))
    # suite.addTest(processTest("test_process63"))
    # suite.addTest(processTest("test_process64"))
    # suite.addTest(processTest("test_process65"))
    # suite.addTest(processTest("test_process66"))
    # suite.addTest(processTest("test_process67"))
    # suite.addTest(processTest("test_process68"))
    # suite.addTest(processTest("test_process69"))
    # suite.addTest(processTest("test_process70"))
    # suite.addTest(processTest("test_process71"))
    # suite.addTest(processTest("test_process72"))
    # suite.addTest(processTest("test_process73"))
    # suite.addTest(processTest("test_process74"))

    runner.run(suite)
    fp.close()
    file_path=new_report("./report/")
    send_mail(file_path)


