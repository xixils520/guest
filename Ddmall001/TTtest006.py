# #   encoding='utf-8'
# import requests
# from bs4 import BeautifulSoup
# user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
# headers={'User-Agent':user_agent}
# r=requests.get('http://seputu.com',headers=headers)
# # print(r.text)
# soup=BeautifulSoup(r.text,'html.parser')
# for mulu in soup.find_all(calss_='mulu'):
#     h2=mulu.find('h2')
#     if h2!=None:
#         h2_title=h2.string
#         for a in mulu.find(class_='box').find_all('a'):
#             href=a.get('href')
#             box_title=a.get('title')
#             print(href,box_title)

'''
第一个示例：简单的网页爬虫

爬取豆瓣首页
'''

# import urllib.request
#
# #网址
# url = "http://www.douban.com/"
#
# #请求
# request = urllib.request.Request(url)
#
# #爬取结果
# response = urllib.request.urlopen(request)
#
# data = response.read()
#
# #设置解码方式
# data = data.decode('utf-8')
#
# #打印结果
# print(data)
#
# #打印爬取网页的各类信息
#
# print(type(response))
# print(response.geturl())
# print(response.info())
# print(response.getcode())
import os
#   encoding='utf-8'
# path='C:\soft\picture'
title='我的文件夹'
path1=os.makedirs(os.path.join('C:/soft/picture'+'/',title))


# path2=os.makedirs(path+'/'+title)
