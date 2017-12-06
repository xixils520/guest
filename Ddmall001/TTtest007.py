#   coding=utf-8
import requests
import re
from urllib.parse import urljoin
from urllib import parse
from bs4 import BeautifulSoup
import codecs

#   url管理器
class UrlManger(object):
    def __init__(self):
        self.new_urls=set()#定义未爬去的
        self.old_urls=set()

    def has_new_self(self):
        return self.new_url_size()!=0
    def get_new_url(self):

        new_url=self.new_urls.pop()

        self.old_urls.add(new_url)

        return new_url
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
    def new_url_size(self):
        return len(self.new_urls)
    def old_url_size(self):
        return len(self.old_urls)

class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        headers={'User-Agent':user_agent}
        r=requests.get(url,headers=headers)

        if r.status_code==200:
            r.encoding='utf-8'
            return r.text
        return None
class HtmlParser(object):
    def parser(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup=BeautifulSoup(html_cont,'html.parser')

        new_urls=self.__get_new_urls(page_url,soup)

        new_data=self.__get_new_data(page_url,soup)

        return new_urls,new_data
    def __get_new_urls(self,page_url,soup):
        new_urls=set()
        links=soup.find_all('a',href=re.compile(r'/python/.*\.html'))
        for link in links:
            new_url=link['href']
            new_full_url=urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    def __get_new_data(self,page_url,soup):
        data={}

        data['url']=page_url
        title=soup.find('head').find('title')

        data['title']=title.get_text()

        summary=soup.find('meta',attrs={'name':'description'})

        data['summary']=summary.get_text()
        return data
class DataOutput(object):
    def __init__(self):
        self.datas=[]
    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    def output_html(self):
        fout=codecs.open('baike.html','w',encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>"%data['title'])
            fout.write("<td>%s</td>"%data['summary'])
            fout.write("</tr>")
            self.datas.remove(data)
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

class SpiderMan(object):
    def __init__(self):
        self.manger=UrlManger()
        self.downloader=HtmlDownloader()
        self.parser=HtmlParser()
        self.output=DataOutput()
    def crawl(self,root_url):
        self.manger.add_new_url(root_url)
        while(self.manger.has_new_self() and self.manger.old_url_size()<1):
            try:
                new_url=self.manger.get_new_url()
                # print(new_url)
                html=self.downloader.download(new_url)
                # print(html)
                new_urls,data=self.parser.parser(new_url,html)

                self.manger.add_new_urls(new_urls)
                self.output.store_data(data)
                print('已抓取%s个链接' % self.manger.old_url_size())
            except Exception as e:
                print('出现异常')
        self.output.output_html()

if __name__=="__main__":
    spider_man=SpiderMan()
    spider_man.crawl("http://www.runoob.com/python/python-variable-types.html")
