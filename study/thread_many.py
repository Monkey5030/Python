# -*- coding: utf-8 -*-

from threading import Thread
from queue import Queue
import requests
from bs4 import BeautifulSoup
import lxml
import os,time,re
from jieba.analyse import *
from concurrent.futures import ThreadPoolExecutor

class DownSpider(Thread):
    def __init__(self,queue,path):
        Thread.__init__(self)
        self.queue=queue
        self.path=path

    def run(self):
        while True:
            url=self.queue.get()
            try :
                download_img(url,path)
            finally:
                self.queue.task_done()


def download_img(url,path):
    res=requests.get(url)
    soup=BeautifulSoup(res.content,'lxml')
    img_list=soup.find_all('img',class_='ui image lazy')
    for img in img_list:
        href=img.get('data-original')
        title=img.get('title')
#        正则替换特殊字符
        strinfo = re.compile(r'[/:*?"<>|\\\(\)]')    # 加r,2个\即可
        title = strinfo.sub('', title)
        l1=list()
#        提取关键词
        for keyword, weight in textrank(title,topK=10, withWeight=True):
#        for keyword, weight in extract_tags(title, withWeight=True):
            l1.append(keyword)
#        print(l1)
        if l1:
            title=l1[0]
        else:
            title

        try:
#            如果存在同名文件，在文件名后追加时间戳，否则直接打开文件
            img_path=path+title+os.path.splitext(href)[-1]
            if os.path.exists(img_path):
                with open(path+title+str(int(time.time()))+os.path.splitext(href)[-1],'wb') as f:
                    img_content=requests.get(href).content
                    f.write(img_content)
            else:
                with open(path+title+os.path.splitext(href)[-1],'wb') as f:
                    img_content=requests.get(href).content
                    f.write(img_content)
        except Exception as e:
            print(e)

        # print(href,title)


if __name__=='__main__':
    url_list=[]
    for i in range(1,5):
        url=f'https://fabiaoqing.com/biaoqing/lists/page/{i}.html'
        url_list.append(url)
    path='./表情包3/'
    #线程池 max_workers指定线程的数量
    start=time.time()
    with ThreadPoolExecutor(max_workers=10) as p:   #类似打开文件,可省去.shutdown()
        future_tasks = [p.submit(download_img, item,path) for item in url_list]
    
    [obj.result() for obj in future_tasks]
    end=time.time()
    spendtime=end-start
    print('此次运行共耗时%s 秒'%spendtime)

#    队列
#    queue=Queue()
#    for thread in range(10):
#        work=DownSpider(queue,path)
#        work.daemon=True
#        work.start()
#
#    for item in url_list:
#        queue.put(item)
#    queue.join()
