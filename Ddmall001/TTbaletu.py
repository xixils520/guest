#   coding=utf-8
# 店铺登录、加入入驻商商品，去结算，提交订单操作
import time
from selenium import webdriver
driver=webdriver.Firefox()
driver.get('http://sh.baletu.com/')
driver.find_element_by_xpath('html/body/div[3]/div/form/ul/li[1]/input').send_keys('张江')
driver.find_element_by_id('index_search').click()