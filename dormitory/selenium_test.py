from selenium import webdriver
import time

def dormitory(uid, upwd, first, second, apply_text):
    driver = webdriver.Chrome('C:/Users/Administrator/Desktop/chromedriver_win32/chromedriver')  # 웹브라우저 chrome
    driver.get("http://dormitory.tu.ac.kr/default/main/main.jsp")
    login_bt = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul[2]/li[2]/a/img')
    login_bt.click()
    # 학번 입력
    tu_id = driver.find_element_by_name('_58_login')
    tu_id.send_keys(uid)
    # 비번 입력
    ut_pw = driver.find_element_by_name('_58_password')
    ut_pw.send_keys(upwd)
    # 로그인 버튼클릭
    tu_submit = driver.find_element_by_id('loginImg')
    tu_submit.click()
    # 외박신청 페이지 클릭
    dormitory_out_apply_bt = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/ul/li[3]')
    dormitory_out_apply_bt.click()
    # ifram으로 전환
    driver.switch_to_frame('iFrameModule')
    # 조회버튼 클릭
    lookup_bt = driver.find_element_by_xpath('//*[@id="btnRetrieveStd"]')
    lookup_bt.click()
    # 외박신청 일자 선택
    apply = driver.find_element_by_name('txtSTAYOUT_REQ_FR_DT')
    apply.click()
    if(first < second):
        first_day = driver.find_element_by_xpath('//*[text() = ' + first + ']')  # text 추출
        first_day.click()
        apply = driver.find_element_by_xpath('//*[@id="txtSTAYOUT_REQ_TO_DT"]')
        apply.click()
        second_day = driver.find_element_by_xpath('//*[text() = ' + second + ']')  # text 추출
        second_day.click()
    else:
        first_day = driver.find_element_by_xpath('//*[text() = ' + first + ']')  # text 추출
        first_day.click()
        apply = driver.find_element_by_xpath('//*[@id="txtSTAYOUT_REQ_TO_DT"]')
        apply.click()
        next_month = driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/a[2]/span')
        next_month.click()
        second_day = driver.find_element_by_xpath('//*[text() = ' + second + ']')  # text 추출
        second_day.click()
    # 외박사유 입력
    text = driver.find_element_by_name('txtBIGO')
    text.send_keys(apply_text)
    # 외박신청 버튼 클릭
    out_apply_submit = driver.find_element_by_name('btnSave')
    out_apply_submit.click()
    alert = driver.switch_to.alert
    alert_txt = alert.text
    alert.accept()
    time.sleep(1)
    driver.quit()
    return alert_txt