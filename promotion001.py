#   coding=utf-8
# 满减活动
import time
from selenium import webdriver
# 登录销售系统
driver=webdriver.Firefox()
driver.get("http://211.152.32.59:31010/users/login")
driver.find_element_by_id("userName").send_keys("13111111111")
time.sleep(1)
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_class_name("login-form-login").click()
time.sleep(3)
print('登录成功后：')
# 选择城市南京
driver.find_element_by_id("supplierUserCityName").find_elements_by_tag_name("option")[3].click()
time.sleep(2)
driver.find_element_by_class_name("btn-success").click()


