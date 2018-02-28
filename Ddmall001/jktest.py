# coding=utf-8
import requests
import json
headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Content-Type':'application/json;charset=UTF-8'}
login_url='http://192.168.1.101:52400/user/login'
login_data='{"username":"12345678910","password":"123456"}'
login_response=requests.post(url=login_url,data=login_data,headers=headers)
data=json.loads(login_response.text)
print (json.dumps(data, sort_keys=True, indent=2,ensure_ascii=False))
