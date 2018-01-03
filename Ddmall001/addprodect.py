#encoding=utf-8
import requests
import json
import time
# 登录全局系统
session=requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type':'application/x-www-form-urlencoded'}
login_url = 'http://192.168.1.251:39000/users/login'
login_data = 'userName=12345678910&password=123456'
login_response = session.post(url=login_url, data=login_data, headers=headers)
# print(login_response.text)
# data = json.loads(login_response.text)
# print(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False))
# 切换城市
wuxi_url='http://192.168.1.251:39000/users/updateAgency'
wuxi_data='cityId=320200&agencyId=17'
city_response=session.post(url=wuxi_url,data=wuxi_data,headers=headers)
print(city_response.text)
i=0
for i in range(5):
# 新增商品
    goods_url='http://192.168.1.251:39000/goods/add'
    goods_data={"brandId":"2436","country":u"中国","name":u'测试ls_'+str(int(time.time())),"catalog":["0","4090100","2"],
                "packType":"0","barCode":str(int(time.time())),"catalogId":"4090100","specification":u"12瓶/箱","unit":u"箱","tax":"17",
                "length":"11","width":"1","height":"1","volume":"11.00","weight":"11","termOfValidity":"365","timeUnit":"2","transProportion":"1",
                "introduction":u"<p>品牌:&nbsp;牛栏山</p ><p>品名:&nbsp;陈酿</p ><p>生产许可证编号：110015010353</p ><p>厂家联系方式：4006179999</p ><p>产地:&nbsp;中国大陆地区</p ><p>省份:&nbsp;北京</p ><p>配料表：纯净水、高粱</p ><p>体积(ml): 600</p ><p>香型：浓香型</p ><p>酒精纯度：中度白酒（40%-50%）</p ><p>度数: 42%Vol</p ><p>食品添加剂：无</p ><p>储藏方法：密闭、干燥、阴凉、常温</p ><p>适用场景:&nbsp;团圆小酌区</p ><p>包装方式:&nbsp;包装</p ><p>包装种类:&nbsp;箱装</p ><p>净含量:&nbsp;500mlX12瓶</p ><p>保质期：180 天</p >"}
    goods_response = session.post(url=goods_url, data=goods_data)
    # print(goods_response.text)
    i=i+1
    time.sleep(4)
    print(i)

