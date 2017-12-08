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
            print(page_url)
            img_html=requests.get(page_url)
            img_Soup=BeautifulSoup(img_html.text,'lxml')
            img_url=img_Soup.find_all('a',attrs={'target':"_blank",'href':True,'class':'pic'})
            # print(img_url)
            for i in img_url:
                print(i)
                print(i.img['src'])
                # name = img_url[-9:-4]
                img=i.img['src']
                name=img[-8:-4]
                img=requests.get(img)
                f=open('C:/soft/picture/'+path+'/'+name+'.jpg','wb')
                f.write(img.content)
                f.close()







