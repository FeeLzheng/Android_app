import os
from appium import webdriver
import datetime
import sys
sys.path.append("C:\\Users\\uni-ubi\\PycharmProjects\\Android_app\\Uface\\test_case")


def insert_img(driver,file_name):
    base_dir=os.path.dirname(os.path.dirname(__file__))
    print(base_dir)
    base_dir=str(base_dir)
    base_dir=base_dir.replace("\\","/")
    base_dir=base_dir.split("/test_case")[0]
    file_path=base_dir+"/report/image"+file_name
    driver.get_screenshot_as_file(file_path)

def modifyTimeTpye(time):
    time1=time.strftime('%Y')
    # #把时间中出现的2位时间转换为1位  如09变9
    time1_m=int(time.strftime('%m'))
    time1_d=int(time.strftime('%d'))
    time1_H=time.strftime('%H:%M')
    date=(time1 + "-" + str(time1_m) + "-" + str(time1_d) + "  " + time1_H)
    return date