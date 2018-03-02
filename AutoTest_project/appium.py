#conding:utf-8
from selenium import webdriver
import os
from appium import webdriver
import time,traceback


desired_caps= {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'huwawei mate8'
desired_caps['app'] = r'E:\app.apk'
desired_caps['appPackage'] = 'com.stjy.jxjy'
desired_caps['appActivity'] = 'com.stjy.jxjy.MainActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

try:

    driver.implicitly_wait(10)
    driver.find_element_by_id('com.stjy.jxjy:id/home_grsz_txt').click()
    driver.find_element_by_id('com.stjy.jxjy:id/login_userName').send_keys('VSCZ100452')
    time.sleep(2)
    driver.find_element_by_id('com.stjy.jxjy:id/login_password').send_keys('123123')
    time.sleep(2)
    driver.find_element_by_id('com.stjy.jxjy:id/login_btn_submit').click()

except:
    print(traceback.format_exc())


input('*** Press to quit..')
driver.quit()




