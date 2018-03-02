from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("http://sh.xsjedu.org/")
time.sleep(1)


js = 'document.getElementById("doyoo_monitor").style.display="none";'

driver.execute_script(js)
