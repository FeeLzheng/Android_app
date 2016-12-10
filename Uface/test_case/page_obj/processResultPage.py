from appium.webdriver.common.mobileby import By
import sys
sys.path.append("C:\\Users\\uni-ubi\\PycharmProjects\\Android_app\\Uface\\test_case\\page_obj")
from base import Page
from time import sleep
import time

class processResult(Page):




    prcess_loc = (By.ID, "com.uniubi.attendance:id/ll_processs")
#申请中栏
    processing_loc=(By.ID,"com.uniubi.attendance:id/process_itemview_description")
    processing_detail_loc=(By.ID,"com.uniubi.attendance:id/tv_process_lv_type")
    processing_detail_backout=(By.ID,"com.uniubi.attendance:id/bt_process_backout")
    processing_sureButton_loc=(By.ID,"android:id/button1")

    processing_detail_title = (By.ID, "com.uniubi.attendance:id/tv_type_text")
    processing_detail_starttime = (By.ID, "com.uniubi.attendance:id/tv_process_start_time")
    processing_detail_endtime = (By.ID, "com.uniubi.attendance:id/tv_process_end_time")
    processing_detail_reason = (By.ID, "com.uniubi.attendance:id/tv_process_reason")
    processing_detial_name = (By.ID, "com.uniubi.attendance:id/tv_process_detail_name")
    processing_detail_status = (By.ID, "com.uniubi.attendance:id/tv_process_detail_type")
#点击菜单栏里的的流程
    def process_click(self):
        self.find_element(*self.prcess_loc).click()
#点击申请中栏目
    def processing_click(self):
        self.find_elements(*self.processing_loc)[0].click()

#点击对应的申请进入详情
    def processing_detail_click(self,type):
        try:
            i=0

            while(i<10):
                title=self.find_elements(*self.processing_detail_loc)[i]

                i=i+1
                if (title.text==type):
                    title.click()
                    break
        except Exception:
            print ("找不到"+type)
#点击撤销
    def processing_detail_backout_click(self):
        self.find_element(*self.processing_detail_backout).click()
#点击确认
    def processing_sureButton(self):
        self.find_element(*self.processing_sureButton_loc).click()

#申请中详情
    def processing_detailInfo_title(self):
        return self.find_element(*self.processing_detail_title).text

    def processing_detailInfo_starttime(self):
        return self.find_element(*self.processing_detail_starttime).text

    def processing_detailInfo_endtime(self):
        return self.find_element(*self.processing_detail_endtime).text

    def processing_detailInfo_reason(self):
        return self.find_element(*self.processing_detail_reason).text

    def processing_detailInfo_name0(self):
        return self.find_elements(*self.processing_detial_name)[0].text

    def processing_detailInfo_name1(self):
        return self.find_elements(*self.processing_detial_name)[1].text

    def processing_detailInfo_status0(self):
        return self.find_elements(*self.processing_detail_status)[0].text

    def processing_detailInfo_status1(self):
        return self.find_elements(*self.processing_detail_status)[1].text

#统一撤销接口
    def processing_detail(self,type):
        sleep(5)
        #点击菜单栏中的流程
        self.process_click()
        #点击申请中
        self.processing_click()
        # 点击对应的申请进入详情
        self.processing_detail_click(type)
    def backout(self):
        #点击撤销
        self.processing_detail_backout_click()
        self.processing_sureButton()
        #返回
        self.driver.keyevent(4)
        sleep(1)


#已通过
    passed_loc=(By.ID,"com.uniubi.attendance:id/process_itemview_description")
    passed_detail_loc=(By.ID,"com.uniubi.attendance:id/tv_process_lv_type")
    passed_detail_title=(By.ID,"com.uniubi.attendance:id/tv_type_text")
    passed_detail_starttime=(By.ID,"com.uniubi.attendance:id/tv_process_start_time")
    passed_detail_endtime = (By.ID, "com.uniubi.attendance:id/tv_process_end_time")
    passed_detail_reason=(By.ID,"com.uniubi.attendance:id/tv_process_reason")
    passed_detial_name=(By.ID,"com.uniubi.attendance:id/tv_process_detail_name")
    passed_detail_status=(By.ID,"com.uniubi.attendance:id/tv_process_detail_type")

#点击已通过
    def passed_click(self):
        self.find_elements(*self.passed_loc)[1].click()

#点击详情
    def passed_detail_click(self,type):
        try:
            i=0

            while(i<10):
                title=self.find_elements(*self.passed_detail_loc)[i].text
                title_click=self.find_elements(*self.passed_detail_loc)[i]
                i=i+1
                if (title==type):
                    title_click.click()
                    break
        except Exception:
            print ("找不到"+type)
#详情信息

    def passed_detialInfo_title(self):
        return self.find_element(*self.passed_detail_title).text

    def passed_detialInfo_starttime(self):
        return self.find_element(*self.passed_detail_starttime).text

    def passed_detialInfo_endtime(self):
        return  self.find_element(*self.passed_detail_endtime).text

    def passed_detialInfo_reason(self):
        return  self.find_element(*self.passed_detail_reason).text

    def passed_detialInfo_name0(self):
        return  self.find_elements(*self.passed_detial_name)[0].text

    def passed_detialInfo_name1(self):
        return  self.find_elements(*self.passed_detial_name)[1].text

    def passed_detialInfo_status0(self):
        passed_detail_status0 = self.find_elements(*self.passed_detail_status)[0].text

    def passed_detialInfo_status1(self):
        passed_detail_status1 = self.find_elements(*self.passed_detail_status)[1].text

#已拒绝
    failed_loc=(By.ID,"com.uniubi.attendance:id/process_itemview_description")
    failed_detail_loc=(By.ID,"com.uniubi.attendance:id/tv_process_lv_type")
    failed_detail_title=(By.ID,"com.uniubi.attendance:id/tv_type_text")
    failed_detail_starttime=(By.ID,"com.uniubi.attendance:id/tv_process_start_time")
    failed_detail_endtime = (By.ID, "com.uniubi.attendance:id/tv_process_end_time")
    failed_detail_reason=(By.ID,"com.uniubi.attendance:id/tv_process_reason")
    failed_detial_name=(By.ID,"com.uniubi.attendance:id/tv_process_detail_name")
    failed_detail_status=(By.ID,"com.uniubi.attendance:id/tv_process_detail_type")

#点击已通过
    def failed_click(self):
        self.find_elements(*self.failed_loc)[2].click()

#点击详情
    def failed_detail_click(self,type):
        i=0
        while(i<10):
            title=self.find_elements(*self.failed_detail_loc)[i].text
            title_click=self.find_elements(*self.failed_detail_loc)[i]
            i=i+1
            if (title==type):
                title_click.click()
                break
#详情信息

    def failed_detialInfo_title(self):
        return self.find_element(*self.failed_detail_title).text

    def failed_detialInfo_starttime(self):
        return self.find_element(*self.failed_detail_starttime).text

    def failed_detialInfo_endtime(self):
        return  self.find_element(*self.failed_detail_endtime).text

    def failed_detialInfo_reason(self):
        return  self.find_element(*self.failed_detail_reason).text

    def failed_detialInfo_name0(self):
        return  self.find_elements(*self.failed_detial_name)[0].text

    def failed_detialInfo_name1(self):
        return  self.find_elements(*self.failed_detial_name)[1].text

    def failed_detialInfo_status0(self):
        return self.find_elements(*self.failed_detail_status)[0].text

    def failed_detialInfo_status1(self):
        return self.find_elements(*self.failed_detail_status)[1].text


#需要我审批

    approving_loc=(By.ID,"com.uniubi.attendance:id/process_itemview_text")
    approving_type_loc=(By.ID,"com.uniubi.attendance:id/tv_process_state")
    approving_name_loc=(By.ID,"com.uniubi.attendance:id/tv_process_lv_type")
    approving_detail_title=(By.ID,"com.uniubi.attendance:id/tv_type_text")
    approving_detail_starttime=(By.ID,"com.uniubi.attendance:id/tv_process_start_time")
    approving_detail_endtime = (By.ID, "com.uniubi.attendance:id/tv_process_end_time")
    approving_detail_reason=(By.ID,"com.uniubi.attendance:id/tv_process_reason")
    approving_detial_name=(By.ID,"com.uniubi.attendance:id/tv_process_detail_name")
    approving_detail_status=(By.ID,"com.uniubi.attendance:id/tv_process_detail_type")
    approving_detail_agree=(By.ID,"com.uniubi.attendance:id/rb_process1")
    approving_detail_hard = (By.ID, "com.uniubi.attendance:id/rb_process2")
    approving_detail_disagree = (By.ID, "com.uniubi.attendance:id/rb_process3")
    approving_detail_noreason = (By.ID, "com.uniubi.attendance:id/rb_process4")
    approving_detail_reconsider = (By.ID, "com.uniubi.attendance:id/rb_process5")
    approving_detail_agreebutton=(By.ID,"com.uniubi.attendance:id/bt_process_agree")
    approving_detail_disagreebutton=(By.ID,"com.uniubi.attendance:id/bt_process_repulse")
    approving_notbutton=(By.ID,"android:id/button2")
    approving_surebutton=(By.ID,"android:id/button1")
    approving_applyier_loc=(By.CLASS_NAME,"android.widget.LinearLayout")

#点击等待我审批
    def approving_click(self):
        self.find_elements(*self.approving_loc)[3].click()

#判断需要请假的人和请假的类型

    def approving_detail_click(self,name,type):
        i=0
        while (i<10):
            n=self.find_elements(*self.approving_name_loc)[i]
            i=i+1
            if (n.text==name):
                j=0
                while(j<10):
                    t = self.find_elements(*self.approving_type_loc)[j]
                    j=j+1
                    if(t.text==type):
                        t.click()
                        break
                break


#需要审批中的详情

    def approving_detialInfo_title(self):
        return self.find_element(*self.approving_detail_title).text

    def approving_detialInfo_starttime(self):
        return self.find_element(*self.approving_detail_starttime).text

    def approving_detialInfo_endtime(self):
        return  self.find_element(*self.approving_detail_endtime).text

    def approving_detialInfo_reason(self):
        return  self.find_element(*self.approving_detail_reason).text

    def approving_detialInfo_name0(self):
        return  self.find_elements(*self.approving_detial_name)[0].text

    def approving_detialInfo_name1(self):
        return  self.find_elements(*self.approving_detial_name)[1].text

    def approving_detialInfo_status0(self):
        return self.find_elements(*self.approving_detail_status)[0].text

    def approving_detialInfo_status1(self):
        return self.find_elements(*self.approving_detail_status)[1].text

    def approving_detailInfo_agree(self):
        self.find_element(*self.approving_detail_agree).click()

    def approving_detailInfo_hard(self):
        self.find_element(*self.approving_detail_hard).click()

    def approving_detailInfo_disagree(self):
        self.find_element(*self.approving_detail_disagree).click()

    def approving_detailInfo_noreason(self):
        self.find_element(*self.approving_detail_noreason).click()

    def approving_detailInfo_reconsider(self):
        self.find_element(*self.approving_reconsider).click()
#点击通过
    def approving_agreebutton_click(self):
        self.find_element(*self.approving_detail_agreebutton).click()

#点击拒绝
    def approving_disagreebutton_click(self):
        self.find_element(*self.approving_detail_disagreebutton).click()

#点击否

    def approving_notbutton_click(self):
        self.find_element(*self.approving_notbutton).click()
#点击是
    def approving_surebutton_click(self):
        self.find_element(*self.approving_surebutton).click()
#选择第二审批人

    def approving_choose_applier(self):
        self.find_elements(*self.approving_applyier_loc)[1].click()



#统一进入审批接口


    def approving(self,name,type):
        sleep(5)
    #点击流程
        self.process_click()
    #点击需要我审批
        self.approving_click()
    #选择需要审批的申请
        self.approving_detail_click(name,type)
        print("观察")

#有第二审批人接口
    def approving_detail1(self,reason,result):
        if (reason=="同意"):
            #点击同意
            self.approving_detailInfo_agree()
        elif (reason=="辛苦"):
            #点击辛苦
            self.approving_detailInfo_agree()
        elif (reason=="拒绝"):
            #点击拒绝
            self.approving_detailInfo_agree()
        elif (reason=="理由不充分"):
            #点击理由不充分
            self.approving_detailInfo_agree()
        elif (reason=="复议"):
            #点击复议
            self.approving_detailInfo_agree()
        else:
            self.approving_detailInfo_agree()

        if(result=="通过"):
            self.approving_agreebutton_click()
            #添加其他审批人
            sleep(2)
            self.approving_surebutton_click()
            sleep(2)
            #选择审批人
            self.approving_choose_applier()
            self.approving_notbutton_click()
            self.approving_choose_applier()
            self.approving_surebutton_click()
            self.keyevent(4)
        else:
            self.approving_disagreebutton_click()
            self.approving_notbutton_click()
            self.approving_disagreebutton_click()
            self.approving_surebutton_click()
            self.keyevent(4)



#无第二审批人接口

    def approving_detail2(self,reason,result):
        if (reason=="同意"):
            #点击同意
            self.approving_detailInfo_agree()
        elif (reason=="辛苦"):
            #点击辛苦
            self.approving_detailInfo_agree()
        elif (reason=="拒绝"):
            #点击拒绝
            self.approving_detailInfo_agree()
        elif (reason=="理由不充分"):
            #点击理由不充分
            self.approving_detailInfo_agree()
        elif (reason=="服役"):
            #点击服役
            self.approving_detailInfo_agree()
        else:
            self.approving_detailInfo_agree()

        if(result=="通过"):
            self.approving_agreebutton_click()
            sleep(2)
            self.approving_notbutton_click()
            self.approving_agreebutton_click()
            self.approving_surebutton_click()
            self.keyevent(4)

        else:
            self.approving_disagreebutton_click()
            sleep(2)
            self.approving_surebutton_click()
            self.keyevent(4)


#已审批

    approved_loc=(By.ID,"com.uniubi.attendance:id/process_itemview_description")




