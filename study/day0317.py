# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:44:30 2021

@author: Admin
"""

from codecs import encode
import pytest
from multiprocessing import Process,Queue,Pool
import math





from requests_html import HTMLSession, AsyncHTMLSession, HTMLResponse
session=HTMLSession()
res=session.get('http://www.xbiquge.la/10/10489/')

links=res.html.absolute_links

#queue = Queue(maxsize=0)
#i=0
#for link in links:
#    queue.put(link)
#    i+=1
    

i=0
    
def save(hrefs):
    for href in hrefs:
        print(href,i)
        res_html=session.get(href)
        head=str(res_html.html.xpath('//*[@id="wrapper"]/div/div/div/h1/text()')).replace('[','').replace(']','').replace('正文卷 ','').replace(' ','').replace("'",'')
        content=str(res_html.html.xpath('//*[@id="content"]/text()'))
        path='d:/code/study/xiaoshuo/'+head+'.txt'
        with open(path,'a+',encoding='utf-8') as f:
            f.write(content)
        i+=1
#        for item in content:
#            f.write(item)
   

if __name__ == '__main__':
#    while queue:
#        href=queue.get()
#        print(href)
##        for i in range(5):
##            p=Process(target=save,args=(href,))
##            p.start()
#        pool = Pool()
#        pool.map(save,links)
#        pool.close()
#        pool.join()
#            
    num = len(links)
    step = 200
    shuliang = math.ceil(num / step)
    flag = 1
    lis = []
    for item in links:
        lis.append(item)
        if (len(lis) == shuliang):
            p = Process(target=save, args=(lis,))
            p.start()
            lis = []
    if (len(lis)):
        p = Process(target=save, args=(lis,))
        p.start()


        
        
