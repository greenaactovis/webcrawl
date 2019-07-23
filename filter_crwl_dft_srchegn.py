from multiprocessing import Pool
import requests
import requests.exceptions
import re
import csv
import pandas as pd
from googlesearch import search
import time
import copy
from itertools import chain
import time
import json
import xlwt
from bs4 import BeautifulSoup
import urllib.request
import re
from tempfile import TemporaryFile
from collections import OrderedDict
from functools import partial
import multiprocessing
link_3 = []
link_4 = []
link_5 = []
link_6 = []
links = []

g = ""
b = ""
d = ""
y = ""
ya = ""
ask = ""

global new_emails
global q
global mail
global all_mails
global no_duplicate
global query
global no_duplicatess
global filtered_links
global mylist
global result_nodup
global newlist
emails = []
new_emails = []
filtered_mail= []
l=[]
mails = []
result_nodup = []
newlist = []
filtered_links = []
all_mails = []
no_duplicate = []
k = []
new_emails = []
mylist = []
email = []
flat = []
flatt = []
def crawl(x,y):   
   try:
      response = requests.get(x)
      s = response.text
      new_emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", s)
      emails.append(new_emails)
   except:
      pass
   flat_list = [item for sublist in emails for item in sublist]
   for i in flat_list:
        email.append(i)
   for i in email:
        if re.search(y , i):
            filtered_mail.append(i)
  
   return filtered_mail  
   
if __name__ == '__main__':
    p = Pool(4)
    q = input("enter the domain:")
##   query2 = ('emails "'+ query + '"' )
##   print(query2)
##   links2 = [j for j in search(query2)]
##   links = list(set(links2))
##   print(links)g=("emails+%22"+q)




    d = "emails+%22"+q+"%22"
    url = "https://duckduckgo.com/?q="+d+"&t=hp&ia=web"
   
    requestd = urllib.request.Request(url)
    responsed = urllib.request.urlopen(requestd)
    html_paged = responsed.read()
    soupd = BeautifulSoup(html_paged,"lxml")
    for link in soupd.findAll('a'):
        link_d = link.get('href')
        d1 = link_d
        link_3.append(d1)



    y = ("emails+%22"+q+"%22")    
    url = "https://in.search.yahoo.com/search?p="+y+"&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8"
    
    request_y = urllib.request.Request(url)
    response_y = urllib.request.urlopen(request_y)
    html_page_y = response_y.read()
    soupy = BeautifulSoup(html_page_y,"lxml")
    for link in soupy.findAll('a'):
        link_y = link.get('href')
        y1 = link_y
        link_4.append(y1)
    

    ya=("emails%20%22"+q+"%22")
    url = "https://yandex.com/search/?text="+ya+"&lr=20983&redircnt=1563447433.1"
    
    request_ya = urllib.request.Request(url)
    response_ya = urllib.request.urlopen(request_ya)
    html_page_ya = response_ya.read()
    soup_ya = BeautifulSoup(html_page_ya,"lxml")
    for link in soup_ya.findAll('a'):
        link_ya = link.get('href')
        ya1 = link_ya
        link_5.append(ya1)
    


    ask=("emails+%22"+q+"%22")
    url = "https://www.ask.com/web?q="+ask+"&o=0&qo=homepageSearchBox"
    
    request_ask = urllib.request.Request(url)
    response_ask = urllib.request.urlopen(request_ask)
    html_page_ask = response_ask.read()
    soup_ask = BeautifulSoup(html_page_ask,"lxml")
    for link in soup_ask.findAll('a'):
        link_ask = link.get('href')
        ask1 = link_ask
        link_6.append(ask1)

    links =  link_3 + link_4 + link_5 + link_6
    print(links)
    nodup_link = list(set(links))
    print(nodup_link)
    string = "https://"
    for i in links:
        if re.search(string , i):
            filtered_links.append(i)
    print(filtered_links)
    linkss = [j for j in filtered_links]
    pool = multiprocessing.Pool(processes=4)
    prod_x=partial(crawl, y=q)
    result_list = pool.map(prod_x, linkss)
    result_copy = result_list
print(result_list)
##newlist = [item for items in result_copy for item in items]
##final_list = list(set(newlist))
##print(final_list)
##book = xlwt.Workbook()
##sheet1 = book.add_sheet('sheet1')
##for i,e in enumerate(final_list):
##    sheet1.write(i,0,e)
##
##name = "random.xls"
##book.save(name)
##book.save(TemporaryFile())

    
    
