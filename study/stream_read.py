#encoding=utf-8

'''
需要安装的包
pymysql
aiomysql
'''
import asyncio
import aiomysql
import pandas as pd
import pymysql
import time
pd.set_option('display.max_rows',None)

# data=pd.DataFrame(columns=['area_code','area_name','level','parent_code'])
# conn=pymysql.connect(host='127.0.0.1',user='root',password='popeye12.', db='work', charset='utf8')
# data=data.append(pd.read_sql('select * from work.area_code_2021 ',conn))
# print(data)


async def dbdaochu(loop):
    # 生成一个空的DataFrame结构
    dd=pd.DataFrame(columns=['area_code','area_name','level','parent_code'])
    sqlstr='select * from work.area_code_2021 limit 100'
    conn = await aiomysql.connect(host='127.0.0.1', user='root',
                           password='popeye12.', db='work', charset='utf8',
                                  loop=loop)
    async with aiomysql.cursors.SSCursor(conn) as cursor:
        await cursor.execute(sqlstr)
        while True:
            row = await cursor.fetchone()
            if not row:
                break
            # 使用元组组成的列表构建DataFrame
            df=pd.DataFrame(data=[row],columns=['area_code','area_name','level','parent_code'])
            # print(df)
            #合并两个DataFrame
            dd=pd.concat([dd,df],ignore_index=True)
        # print(dd)
        return dd

        # data=data1.append(row)
    # return data1	

            
    
if __name__ == '__main__':
    start=time.time()
    loop = asyncio.get_event_loop()
    data2=loop.run_until_complete(dbdaochu(loop))
    # data2.to_excel("location.xlsx",encoding="gbk",index=False )
    # 删除第一行
    # data2.drop(data2.index[0],inplace=True)
    # data2.to_csv("location.csv",encoding="gbk",index=False )
    print(data2)
    end=time.time()
    print('此次执行共花费%s s'%(end-start))
    loop.close()
