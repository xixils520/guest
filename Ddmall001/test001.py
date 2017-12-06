# def local_test():
#     def do_local():
#         a='do'
#     def do_nonlocal():
#         nonlocal a
#         a='nonlocal a'
#     def do_global():
#         global a
#         a='global a'
#     a = 'waibu'
#     do_local()
#     print(a)
#     do_nonlocal()
#     print(a)
#     do_global()
#     print(a)
# local_test()
# print(a)
#   coding=utf-8
import requests
import re
from urllib.parse import urljoin
from urllib import parse
from bs4 import BeautifulSoup
import codecs
# class DataOutput(object):
#     def __init__(self):
#         self.datas=['http://www.runoob.com/python/python-variable-types.html']
#         print(self.datas)
#     def store_data(self,data):
#         if data is None:
#
#             return
#         self.datas.append(data)
def output_html(datas):
    fout=codecs.open('baike.html','w',encoding='utf-8')
    fout.write("<html>")
    fout.write("<body>")
    fout.write("<table>")
    for data in datas:
        fout.write("<tr>")
        fout.write("<td>%s</td>"%data['url'])
        fout.write("<td>%s</td>"%data['title'])
        fout.write("<td>%s</td>"%data['summary'])
        fout.write("</tr>")
        datas.remove(data)
    fout.write("</table>")
    fout.write("</body>")
    fout.write("</html>")
    fout.close()
output_html(['http://www.runoob.com/python/python-variable-types.html'])


