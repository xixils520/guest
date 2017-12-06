#   encoding=utf-8
import requests
from bs4 import BeautifulSoup
import os
import re
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
for a in all_a:
    title=a.get_text()
    path=str(title).strip()
    path=re.search('\w+',path).group()
    if not os.path.exists('C:/soft/picture/'+path):
        os.makedirs('C:/soft/picture/' + path)
        os.chdir('C:/soft/picture/' + path)
    href=a['href']
    # print(title,href)
    html=requests.get(href,headers=headers)
    html_Soup=BeautifulSoup(html.text,'lxml')
    max_span=html_Soup.find('div',class_='pagenavi').find_all('span')[-2].get_text()
    for page in range(1,int(max_span)+1):
        page_url=href+'/'+str(page)

        img_html=requests.get(page_url,headers=headers)
        img_Soup=BeautifulSoup(img_html.text,'lxml')
        img_url=img_Soup.find('div',class_='main-image').find('img')['src']
        name=img_url[-9:-4]
        img=requests.get(img_url,headers=headers)
        f=open('C:/soft/picture/'+path+'/'+name+'.jpg','wb')
        f.write(img.content)
        f.close()
