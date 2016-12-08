import os
from appium import webdriver

def insert_img(driver,file_name):
    base_dir=os.path.dirname(os.path.dirname(__file__))
    print(base_dir)
    base_dir=str(base_dir)
    base_dir=base_dir.replace("\\","/")
    base_dir=base_dir.split("/test_case")[0]
    file_path=base_dir+"/report/image"+file_name
    driver.get_screenshot_as_file(file_path)

