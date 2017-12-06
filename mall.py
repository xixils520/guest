#   coding=utf-8
# 店铺登录、加入今日主打商品，去结算，取消订单操作
import time
from selenium import webdriver
# 正常账号密码商城登录验证
driver=webdriver.Firefox()
driver.get("http://211.152.32.59:30011/login")
driver.find_element_by_id("uid").send_keys("15365255217")
time.sleep(1)
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
print("店铺名称是："+stores_user)
# 返回首页
driver.back()
time.sleep(1)
# 刷新当前页面
driver.refresh()
time.sleep(3)
# 进入今日主打商品页面
driver.find_element_by_class_name("good-title").click()
# 今日主打商品加入购物车
driver.find_element_by_class_name("add-good-cart").click()
# 进入购物车
time.sleep(5)
driver.find_element_by_id("link_cart").click()
time.sleep(2)
# driver.find_element_by_class_name("checkout_button").click()
# 点击去结算
driver.find_element_by_xpath(".//*[@id='total']/div[2]/button").click()
time.sleep(3)
# # 选中支付方式：货到付款
# driver.find_element_by_xpath(".//*[@id='cart_preview']/div[7]/div/div[1]").click()
# 获取商品数量
good_amount=driver.find_element_by_xpath(".//*[@id='good_element_152064']/div[3]/span").text
print("商品数量是："+good_amount)
# 获取商品价格
good_price=driver.find_element_by_xpath(".//*[@id='good_element_152064']/div[4]/div/span").text
print(good_price)
good_price_int=float(good_price[1:])
print("商品价格是"+good_price)
# 获取达豆抵扣金额
dadou=driver.find_element_by_xpath(".//*[@id='dadou_amount']").text
print(dadou)
dadou_int=float(dadou[3:])
print("达豆抵扣金额是"+dadou)
# 计算商品价格
order_price=good_price_int-dadou_int
print(order_price)
# 获取支付价格
price=float(driver.find_element_by_xpath(".//*[@id='final_price']").text)
if order_price==price:
    print("订单价格计算正确")
else:
    print("订单价格计算不正确")
# 提交订单
driver.find_element_by_xpath(".//*[@id='checkout_button']/button").click()
time.sleep(5)
# 查看订单
driver.find_element_by_xpath(".//*[@id='app_page']/div[3]/div/div[2]/div/div[3]/div[2]/a").click()
time.sleep(5)
# 取消订单
driver.find_element_by_xpath(".//*[@id='order_all']/div[1]/div[1]/div[1]/div[3]/div[2]/span").click()
driver.find_element_by_xpath(".//*[@id='submit_cancel']").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='alert_modal_close']").click()
driver.quit()