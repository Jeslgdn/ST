from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.switch_to_frame()
driver.get('http://www.baidu.com')

em = driver.find_element_by_id("head_wrapper")
print(em.get_attribute("innerHTML"))

