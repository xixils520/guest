# encoding=utf-8
from pymongo import MongoClient
from datetime import datetime
import time
client = MongoClient()
db = client['sjk']
db_name = db['mymongodb']
title = '0'
url = 'www.dd528.com'
time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
i=0
for i in range(5,30,5):


    post = {
        '标题': i,
        '主题页面': url,
        '图片地址': url,
        '获取时间': time
        }

    if i==10:
        break
    i=i+1
    print(i)
    db_name.insert(post)

# db_name.update({'标题': '新的存入数据'},{'$set':{"获取时间":datetime.now()}})
print(time)
# db_name.remove()

