#encoding=utf-8

from threading import Thread
from queue import Queue
import requests
from bs4 import BeautifulSoup
import lxml
import os

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
        title=img.get('title').split('/')[0].replace('?','')[:10]
        try:
            if os.path.splitext(href)[-1]!='.gif':
                with open(path+title+os.path.splitext(href)[-1],'wb') as f:
                    img_content=requests.get(href).content
                    f.write(img_content)
        except Exception as e:
            print(e)

        # print(href,title)


if __name__=='__main__':
    url_list=[]
    for i in range(1,200):
        url=f'https://fabiaoqing.com/biaoqing/lists/page/{i}.html'
        url_list.append(url)
    path='./表情包3/'

    queue=Queue()


    for thread in range(10):
        work=DownSpider(queue,path)
        work.daemon=True
        work.start()

    for item in url_list:
        queue.put(item)
    queue.join()
