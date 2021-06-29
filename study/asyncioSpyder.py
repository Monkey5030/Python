import asyncio
import os
import re
import time

import ahttp
import aiofiles
import aiohttp
import requests
from bs4 import BeautifulSoup
from jieba.analyse import textrank
from requests_html import AsyncHTMLSession,HTMLSession
from queue import Queue

hrefs=[]
urls=set()

async def clean(url,path,semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as s1:
            async with s1.get(url) as response:
                res=await response.content.read()
                res=res.decode('utf-8','ignore')
                soup=BeautifulSoup(res,'lxml')
                img_list=soup.find_all('img',class_='ui image lazy')
                for img in img_list:
                    href = img.get('data-original')
                    title = img.get('title')
                    #        正则替换特殊字符
                    strinfo = re.compile(r'[/:*?"<>|\\\(\)]')  # 加r,2个\即可
                    title = strinfo.sub('', title)
                    l1 = list()
                    hrefs.append(href)
                    #        提取关键词
                    for keyword, weight in textrank(title, topK=10, withWeight=True):
                        #        for keyword, weight in extract_tags(title, withWeight=True):
                        l1.append(keyword)
                    #        print(l1)
                    if l1:
                        title = l1[0]
                    else:
                        title
                    urls.add(url)

                    try:
                        #            如果存在同名文件，在文件名后追加时间戳，否则直接打开文件
                        img_path = path + title + os.path.splitext(href)[-1]


                        async with aiohttp.ClientSession(headers=headers) as session:
                            async with session.get(href) as response:
                                async with aiofiles.open(path + title + os.path.splitext(href)[0].split('/')[-1] + os.path.splitext(href)[-1], 'wb') as f:
                                    await f.write(await response.content.read())

                    except Exception as e:
                        print(e)
                return url, img_list


async def main():
    # tasks = []
    urls=[f'https://fabiaoqing.com/biaoqing/lists/page/{i}.html' for i in range(1,201)]
    # for url in urls:
    #        tasks.append(asyncio.create_task(clean(url,path)))
    #
    # await asyncio.wait(tasks)
    semaphore = asyncio.Semaphore(6)  # 限制并发量为500
    tasks = [clean(url,path,semaphore) for url in urls]
    # 并发执行并保存每一个任务的返回结果
    results = await asyncio.gather(*tasks)
    print([item[0] for item in results if item[1]])





if __name__ == '__main__':
    path='./表情包4/'
    start=time.time()
    loop = asyncio.get_event_loop()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    }
    asyncio.run(main())
    print(len(list(urls)), urls)

    spend=time.time()-start
    print('花费时间为：%s S'%spend)
