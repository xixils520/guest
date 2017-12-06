# encoding: utf-8
import urllib.request
import sys,io
from imp import reload
reload(sys)

#抓取起点页面内容
def gethtml(url):
    """
    获取整个页面的内容
    :param url:
    :return:
    """
    txt2=urllib.urlopen(url)
    html = txt2.read()
    #print html
    return html


def thread_pool( l):
    """
    准备线程池请求接口
    :param l: 接口列表
    :return:
    """

    try:
        url_start(l)
    except IndexError:
        print('IndexError url:\n' + l)


def get_content(html):
    """
    文章内容获取
    :param html:
    :return:
    """
    title=get_title(html)
    #文章内容
    content_re= re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*)<')
    #content = re.findall(content_re,html)
    content=re.findall(content_re,html.decode('gbk'))
    #print content
    re_h=re.compile('</?\w+[^>]*>')#HTML标签
    #换行符转换
    #br_re=re.compile('<br>')
    fp.write('\n'+ title)
    fp.write('\n'+u"======================================"+'\n')
    content1=''
    for i in content:#此处要这样输出，要不然会有乱码
        i=re.sub(re_h,'',i)
        re_g=re.compile('&nbsp;')
        i=re.sub(re_g,'',i)
        #i3=str(i.strip())
        fp.write(i+ '\n')
        content1=content1+i

    return content1

def get_title(html):
    """
    获取标题
    :param html:
    :return:
    """
    #标题  那标题
    title_re=re.compile('<h1>(.*?)</h1>')
    title=re.search(title_re,html.decode('gbk'))
    title=title.group(1).replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('>','').replace('<','').replace('|','').replace(' ','')
    print(title)
    return title

def url_start(html):
    """
     执行写入数据的接口
    :param html:
    :return:
    """
    try:
        print (html)
        html_content = gethtml(html)
        get_content(html_content)
    except:
        print("请求地址不存在 404报错 请求下一个")

def url_directory(html):
    """
    获取小说目录地址的url
    :param html:
    :return:
    """
    l= []
    content_re = re.compile(' <dd><a href="(.*?)">')
    content = re.findall(content_re, html.decode('gbk'))
    content1 = ''
    for i in content:  # 此处要这样输出，要不然会有乱码
        l.append(i)
        content1 = content1 + i  #所有章节链接后半部分
        #print content1
    return l

if __name__=='__main__':
    """
    这个主要抓取的是起点网站的数据根据目录 然后抓取这些内容
    """
    url2='http://www.00ksw.com/html/3/3210/' #通过拼接的方式获取网页元素

    html_content = gethtml(url2)
    #print html_content
    title = get_title(html_content) #获取小说名称
    #print title
    #重命名文本--写入小说标题和内容
    fp = io.open(u'%s.txt' % title, 'a', encoding='utf-8')  #写小说名称
    l=url_directory(html_content) #获取目录地址 比如 1.html  2.html
    for i in l:
        html = url2 + i
        thread_pool(html) #写入标题和内容数据
    #关闭写入数据
    fp.close()