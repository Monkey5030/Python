# encoding=utf-8
# 作者：Admin
# 日期：2021/6/16 15:53
# 工具：PyCharm

'''
CREATE TABLE `cnblog` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` tinytext COLLATE utf8mb4_croatian_ci,
  `url` varchar(200) COLLATE utf8mb4_croatian_ci DEFAULT NULL,
  `summary` text CHARACTER SET utf8mb4 COLLATE utf8mb4_croatian_ci,
  `postdate` varchar(100) COLLATE utf8mb4_croatian_ci DEFAULT NULL,
  `view` int DEFAULT NULL,
  `comment` varchar(200) COLLATE utf8mb4_croatian_ci DEFAULT NULL,
  `digg` int DEFAULT NULL,
  `source_url` varchar(255) COLLATE utf8mb4_croatian_ci DEFAULT NULL,
  `insert_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url` (`url`)
) ENGINE=InnoDB AUTO_INCREMENT=3061 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_croatian_ci

'''

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re
from pprint import pprint
import csv
import json
import pymysql
import time
import datetime
from concurrent.futures import ThreadPoolExecutor
# 导入线程池模块
import threading

class mysql_func():
    def get_data(db, sql, data=None):
        try:
            curors = db.cursor()
        except:
            db.ping(reconnect=True)
            curors = db.cursor()

        if data == None:
            curors.execute(sql)
        else:
            curors.executemany(sql, data)
        db.commit()
        data = curors.fetchall()
        curors.close()
        return data

    def get_row_number(db, sql, data=None, type=1):
        try:
            curors = db.cursor()
        except:
            db.ping(reconnect=True)
            curors = db.cursor()
        if data is not None and type == 1:
            curors.executemany(sql, data)
        elif data is None:
            curors.execute(sql)
        else:
            curors.execute(sql, data)
        db.commit()
        data = curors.rowcount
        curors.close()
        # db.close()
        return data

    def get_json(db, sql, data=None):
        try:
            curors = db.cursor()
        except:
            db.ping(reconnect=True)
            curors = db.cursor()
        if data == None:
            curors.execute(sql)
        else:
            curors.executemany(sql, data)
        db.commit()
        columns = [col[0] for col in curors.description]

        def dict_fetchall(cursor):
            "Return all rows from a cursor as a dict"
            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

        data = dict_fetchall(curors)
        curors.close()
        return data


ua=UserAgent()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'cookie': '__gads=ID=a367abe7a825dc87-2253269c97c500a8:T=1610017075:S=ALNI_MZVqSWdd4OK2wYB_kJgnIiYJxwqYg; UM_distinctid=1796482436066-038f1bb6f4c4ed-52301645-1fa400-17964824361b7f; .CNBlogsCookie=36A06E805F33433C2C270973BD15FE3971ADDF9E961F774D84A4ACA7AA45054BF0178035888CC80FCA0F2595792782C664B75FC0F33F3FBC52242FF8234E4CB6CD594741C8959497528437ABA1E5D54F4DF0DA33; _gid=GA1.2.1509652053.1623719423; __utma=226521935.1882738310.1609749355.1623816027.1623816027.1; __utmc=226521935; __utmz=226521935.1623816027.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=59123430; .Cnblogs.AspNetCore.Cookies=CfDJ8L-rpLgFVEJMgssCVvNUAjstSAoHdw2ZAUbg_AhGeGGNAmMgnqrw113Ak1aRUOuIRp4soLeIcLdzs_7Vj-lboCgsdcLYKCwOLRcCvQxomxScrKQ251roz8comolrFTv4_PWfIVjaJRQBy3CbTuyFPeS7Yo7HmUzJeoxhAViUqFptMq6lmi2W4s-Gr8od-e6nda7hxDTXtuMhCGB_fo20TqSdy5s3C6FXjj4fv_W3EYSlIjERdeBdzF_3qqCUrM0iKkHUrTbXsyyg3qt1Op3ezeQNCMSXCIqCTVGAH0q8bYZFR8LhW7OapdRd6rMzrCPJJnCN460LD_ZbBzIUsOqYQcjL7l9PBRWMaDgAUvjaQbL7e-zjIkMSrhSXtuxs2_6UnOMs297pNDunCTQRqa4ryHWJgBmSGoGepgOKtzzW6IfIGyV7ivKaENZgKQJ1pbjHHh-H95xFeD5eGjVqLAn5KzhHeSJdu5g_C3UORTe0eCgXsY8G5wtJvZ_YqHoF8jYvUDnop0l2hinfEC62oMiRCV8cKKu9UFb8EXu-aTcRcOykc9_os3qd0nbwNTThrBBn4w; _ga_4CQQXWHK3C=GS1.1.1623901692.4.0.1623901692.0; _ga=GA1.2.1882738310.1609749355; __utmz=59123430.1623902297.4.4.utmcsr=cnblogs.com|utmccn=(referral)|utmcmd=referral|utmcct=/pick/; __utma=59123430.1882738310.1609749355.1623892752.1623902296.4'
}
list_all=list()
def get_info(url):
    print(url)
    html = requests.get(url, headers=headers)
    soup=BeautifulSoup(html.text.encode('utf-8').decode('utf-8'),'lxml')
    try:
        list1 = [[item.find(class_='searchItemTitle').get_text().replace('\n',''),
                 re.findall('href="(([\s\S]*.html)")', str(item.find(class_='searchItemTitle')))[0][0],
                  item.find(class_='searchCon').get_text().replace('\n',''),
                  item.find(class_='searchItemInfo-publishDate').get_text(),
                  re.findall('\d+', str(item.find(class_='searchItemInfo-views')))[0],
                 0,
                  0,
                  # re.findall('\d+', str(item.find(class_='searchItemInfo-good')))[0],
                  url,
                  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                  ]
                    for item in
                  soup.find_all(class_='searchItem')]
    except Exception as e:
        print(e)
        print(soup.find_all(class_='searchItem'))
        print(123,url,'#'*100)
    return list1


def save(url):
 # with open(filename,'w',encoding='utf-8-sig',newline='') as f:
 #  csv_writer = csv.writer(f)
 #  csv_writer.writerow(['标题', '网址', '摘要', '发布时间', '阅读量', '评论', '推荐'])
 #  for item in response:
 #   csv_writer.writerow([column.replace('\n', '') for column in item])
    response = get_info(url)
    print(response)
    db = pymysql.connect(user="root", password="popeye12.", host="127.0.0.1", port=3306,
                      database="work")
    try:
        insert_sql = """ insert ignore into work.cnblog (title,url,summary,postdate,view,comment,digg,source_url,insert_date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        print(mysql_func.get_row_number(db, insert_sql, response))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    url='https://zzk.cnblogs.com/s/blogpost?Keywords=python%E7%88%AC%E8%99%AB&pageindex='
    urllist=[url+str(item) for item in range(1,51)]
    with ThreadPoolExecutor(max_workers=10) as p:  # 类似打开文件,可省去.shutdown()
        future_tasks = [p.submit(save, i) for i in urllist]
    print('=' * 150)
    print([obj.result() for obj in future_tasks])

