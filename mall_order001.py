#   coding=utf-8
# 店铺登录、加入入驻商商品，去结算，提交订单操作
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException
# 正常账号密码商城登录验证
driver=webdriver.Firefox()
driver.get("http://192.168.1.251:30011/login")
driver.find_element_by_id("uid").send_keys("987654321")
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
driver.get("http://192.168.1.251:30011/detail?gid=125732")
driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").click()
driver.get("http://192.168.1.251:30011/detail?gid=125735")
driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div[1]/div/div[5]/div[2]/button").click()
# time.sleep(5)
try:
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"link_cart")))
finally:
    driver.find_element_by_id("link_cart").click()
# driver.find_element_by_class_name("checkout_button").click()
# 点击去结算

time.sleep(3)
driver.find_element_by_xpath(".//*[@id='total']/div[2]/button").click()
time.sleep(3)
# 获取商品数量
good_amount=driver.find_element_by_xpath(".//*[@id='good_element_125735']/div[3]/span").text
print("商品数量是："+good_amount)
# 获取商品价格
good_price=driver.find_element_by_xpath(".//*[@id='good_element_125735']/div[4]/div/span").text
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
#   选中支付方式：货到付款
# driver.find_element_by_xpath(".//*[@id='cart_preview']/div[7]/div/div[1]").send_keys(Keys.TAB)
target=driver.find_element_by_xpath(".//*[@id='cart_preview']/div[7]/div/div[1]")
driver.execute_script("arguments[0].scrollIntoView();", target)
driver.find_element_by_xpath(".//*[@id='cart_preview']/div[7]/div/div[1]").click()
time.sleep(3)
# 提交订单
driver.find_element_by_xpath(".//*[@id='checkout_button']/button").click()
time.sleep(3)
# 登录客服系统审核订单
driver.get("http://192.168.1.251:3586/service/manager")
driver.find_element_by_xpath("html/body/div[1]/div[2]/div/form/div/input[1]").send_keys("12345678910")
driver.find_element_by_xpath(".//*[@id='password']").send_keys("123456")
driver.find_element_by_xpath("html/body/div[1]/div[2]/div/form/input").click()
time.sleep(3)
driver.find_element_by_id("agencyName").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_xpath(".//*[@id='confirm-new']").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='stores_order_date']/div[3]/span[4]/button").click()
# 获取订单编号
driver.find_element_by_xpath(".//*[@id='stores_order_query']").click()
time.sleep(3)
order_code=driver.find_element_by_xpath(".//*[@id='store_order_data_element']/tr[2]/td[2]").text
print(order_code)
driver.find_element_by_xpath(".//*[@id='select_all_order_checkbox']").click()
driver.find_element_by_xpath(".//*[@id='send_stores_orders_button']").click()
time.sleep(3)
# 登录仓库运输系统，出库商品
driver.get("http://192.168.1.243:48000/users/login?path=/expressRoute/create/tail")
driver.find_element_by_xpath("html/body/div[1]/div[2]/div/form/div/input[1]").send_keys("12345678910")
driver.find_element_by_xpath(".//*[@id='password']").send_keys("123456")
driver.find_element_by_xpath("html/body/div[1]/div[2]/div/form/input").click()
time.sleep(3)
driver.find_element_by_id("supplierUserCityName").find_elements_by_tag_name("option")[1].click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='alert-modal']/div/div/div[3]/span[2]").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='side-menu']/li[3]/a").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='762']/li[1]/a").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='orderTime']").click()
time.sleep(3)
driver.find_element_by_xpath("html/body/div[3]/div[1]/table/tfoot/tr/th").click()
time.sleep(3)
driver.find_element_by_xpath("html/body/div[2]/div[1]/div/button").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='762']/li[3]/a").click()
time.sleep(3)
# 获取波次号
bc_id=driver.find_element_by_xpath(".//*[@id='expressRoute_views_table']/tbody/tr[1]/td[2]").text
print(bc_id)
driver.find_element_by_xpath(".//*[@id='expressRoute_views_table']/tbody/tr[1]/td[7]/span[2]").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='762']/li[4]/a").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='modal']/div/div/div[3]/button").click()
driver.find_element_by_xpath("html/body/div[2]/div[1]/div[1]/div[2]/input").send_keys(bc_id)
driver.find_element_by_xpath(".//*[@id='btn-search']").click()
time.sleep(3)
driver.find_element_by_css_selector("[func='confirmPickList']").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='pick-good-name']").send_keys("李松")
driver.find_element_by_xpath(".//*[@id='complete-confirm']").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='modal']/div/div/div[3]/button").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='762']/li[5]/a").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='express-route-order-scanf-input']").send_keys(order_code)
driver.find_element_by_xpath(".//*[@id='express-route-order-scanf']").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='review-finish']").click()
time.sleep(5)
driver.find_element_by_xpath(".//*[@id='762']/li[6]/a").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='order-express-scanf-out-base-input']").send_keys("7777")
driver.find_element_by_xpath(".//*[@id='order-express-scanf-out-base-confirm']").click()
driver.find_element_by_xpath(".//*[@id='order-express-scanf-out-base-input']").send_keys(order_code)
driver.find_element_by_xpath(".//*[@id='order-express-scanf-out-base-confirm']").click()
driver.find_element_by_xpath(".//*[@id='order-express-scanf-out-confirm']").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='add-goods-modal-form-confirm']").click()
time.sleep(5)
driver.back()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='side-menu']/li[6]/a").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='788']/li[3]/a").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='waited-table']/tbody/tr/td[9]/button").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='truck-unload-detail-modal']/div/div/div[2]/button[1]").click()
driver.find_element_by_xpath(".//*[@id='truck-unload-detail-modal']/div/div/div[2]/button[3]").click()
driver.quit()
# def find_element(element):
#     try:
#         time.sleep(1.5)
#         driver.implicitly_wait(5)
#         WebDriverWait(driver,12,1).until(lambda driver: driver.find_element_by_xpath(element).is_displayed())
#         # WebDriverWait(driver,12,1).until(EC.presence_of_element_located(element))
#         return driver.find_element_by_xpath(element)
#     except NoSuchElementException as e:
#
#         time.sleep(3)
#         driver.implicitly_wait(5)
#         return driver.find_element_by_xpath(element)