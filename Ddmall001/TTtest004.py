#   encoding=utf-8
import requests
from bs4 import BeautifulSoup
import os
import re
from Ddmall001.TTtest008 import Download
from Ddmall001.TTtest008 import request
from Pymo
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36','Referer':'http://www.mzitu.com/99566'}
all_url='http://www.mzitu.com/all/'
start_html=requests.get(all_url,headers=headers)
# print(start_html.text)
Soup=BeautifulSoup(start_html.text,'lxml')
# li_list=Soup.find_all('li')
# li_list=Soup.find('div',class_='all').find_all('a')
# for li in li_list:
#     print(li)
all_a=Soup.find('div',class_='all').find_all('a')
# for a in all_a:
#     title=a.get_text()
#     path=str(title).strip()
#     path=re.search('\w+',path).group()
#     if not os.path.exists('C:/soft/picture/'+path):
#         os.makedirs('C:/soft/picture/' + path)
#         os.chdir('C:/soft/picture/' + path)
#     href=a['href']
#     # print(title,href)
#     html=requests.get(href,headers=headers)
#     html_Soup=BeautifulSoup(html.text,'lxml')
#     max_span=html_Soup.find('div',class_='pagenavi').find_all('span')[-2].get_text()
#     for page in range(1,int(max_span)+1):
#         page_url=href+'/'+str(page)
#
#         img_html=requests.get(page_url,headers=headers)
#         img_Soup=BeautifulSoup(img_html.text,'lxml')
#         img_url=img_Soup.find('div',class_='main-image').find('img')['src']
#         name=img_url[-9:-4]
#         img=requests.get(img_url,headers=headers)
#         f=open('C:/soft/picture/'+path+'/'+name+'.jpg','wb')
#         f.write(img.content)
#         f.close()
class mzitu():

    def all_url(self,url):
        html=request.get(url,3)
        all_a=BeautifulSoup(html.text,'lxml').find('div',class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            print(u'开始保存：',title)
            path = str(title).strip()
            path = re.search('\w+', path).group()
            self.mkdir(path)
            # os.makedirs('C:/soft/picture/' + path)

            # if not os.path.exists('C:/soft/picture/' + path):
            #     os.makedirs('C:/soft/picture/' + path)
            #     os.chdir('C:/soft/picture/' + path)
            os.chdir('C:/soft/picture/' + path)
            href = a['href']
            self.html(href)
    def html(self,href):
        html=request.get(href,3)
        max_span = BeautifulSoup(html.text,'lxml').find_all('span')[10].get_text()
        for page in range(1,int(max_span)+1):
            page_url=href+'/'+str(page)
            self.img(page_url)
    def img(self,page_url):
        img_html=request.get(page_url,3)
        img_url=BeautifulSoup(img_html.text,'lxml').find('div',class_='main-image').find('img')['src']
        self.save(img_url)
    def save(self,img_url):
        name=img_url[-9:-4]
        print(u'开始保存',img_url)
        img=request.get(img_url,3)
        f=open(name+'.jpg','wb')

        f.write(img.content)
        f.close()
    def mkdir(self,path):
        path=path.strip()
        isExists=os.path.exists(os.path.join('C:/soft/picture/',path))
        if not isExists:
            print(u'新建文件夹',path)
            os.makedirs('C:/soft/picture/' + path)
            return True
        else:
            print(u'文件夹已存在')
            return False

Mzitu=mzitu()
Mzitu.all_url('http://www.mzitu.com/all')