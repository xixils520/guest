#   coding=utf-8
import time
from selenium import webdriver
# 正常账号密码商城登录验证
driver=webdriver.Chrome()
driver.get("http://www.dd528.com")
driver.find_element_by_id("uid").send_keys("17192180663")
driver.find_element_by_id("pwd").send_keys("123456")
driver.find_element_by_id("login_submit").click()
time.sleep(3)
print('登录成功后：')
# 打印当前title
title=driver.title
print(title)
# 打印当前url
now_url=driver.current_url
print(now_url)
# 进入个人中心
driver.find_element_by_link_text("个人中心").click()
time.sleep(3)
# 获取登录店铺名称
#storesuser=driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div")
stores_user=driver.find_element_by_css_selector("[class='container-content content-t']").text
print(stores_user)
driver.quit()