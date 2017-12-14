#   coding=utf-8
# from multiprocessing import Pool
# import os,time,random
# def run_task(name):
#     print('Task %s (%s)...' % (name, os.getpid()))
import os
from bs4 import BeautifulSoup
import requests
import re
html='http://www.tooopen.com/img/87_312.aspx'
url=requests.get(html)
# print(url.text)
soup=BeautifulSoup(url.text,'lxml')
url=soup.find('div',class_='cell type-list first-cell').find_all('a')
# print(url)
for a in url:
    name=a.get_text()
    # print(name)
    path = str(name).strip()
    # print(path)
    href=a['href']
    # print (a['href'])
    if not os.path.exists('C:/soft/picture/' + path):
        os.makedirs('C:/soft/picture/' + path)
        os.chdir('C:/soft/picture/' + path)
        for page in range(1, len(url) + 1):
            page_url='http://www.tooopen.com'+href
            # print(page_url)
            img_html=requests.get(page_url)
            img_Soup=BeautifulSoup(img_html.text,'lxml')
            img_url=img_Soup.find_all('a',attrs={'target':"_blank",'href':True,'class':'pic'})
            # print(img_url)
            for i in img_url:
                # print(i)
                # print(i.attrs.keys())
                href=i['href']
                print(href)
                img = requests.get(href)
                img_Soup=BeautifulSoup(img.text,'lxml').find('div',class_='hindendiv').find('a',attrs={'data-img':True})
                # print(img_Soup)
                # print(img_Soup.attrs.keys())
                img=img_Soup['data-img']
                print(img)
                # print('1111111111')
                name = img[-8:-4]
                img = requests.get(img)
                # print('22222222222')

                f = open('C:/soft/picture/' + path + '/' + name + '.jpg', 'wb')
                # print('3333333')
                f.write(img.content)
                # print('44444444')
                f.close()




                # if 'scr' in i.img.attrs.keys():
                #
                #     img=i.img['src']
                #     print('11111111111')
                #     print(img)
                #     name = img[-8:-4]
                #     img = requests.get(img)
                #     f = open('C:/soft/picture/' + path + '/' + name + '.jpg', 'wb')
                #     f.write(img.content)
                #     f.close()
                # elif 'data-src' in i.img.attrs.keys():
                #     img = i.img['data-src']
                #     print('2222222')
                #     print(img)
                #     name = img[-8:-4]
                #     img = requests.get(img)
                #     f = open('C:/soft/picture/' + path + '/' + name + '.jpg', 'wb')
                #     f.write(img.content)
                #     f.close()
                #
                # else:
                #     img=''









