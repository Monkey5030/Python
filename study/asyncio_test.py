#encoding=utf-8

import asyncio
import aiomysql
import pymysql

table_dict=dict()
async def get_num(tablename):
    conn1 = await aiomysql.connect(host='127.0.0.1', port=3306, user='root', password='popeye12.', db='work', )
    cur1 = await conn1.cursor()
    select_sql='select count(1) from %s '%tablename
    try:
        await cur1.execute(select_sql)
        num=await cur1.fetchone()
        print(f'{tablename}:\t{num[0]}')
        table_dict.update({tablename:num[0]})
    except Exception as e:
        print(e)
    await cur.close()
    conn.close()


async def main():
    tasks = [asyncio.create_task(get_num(host[0])) for host in res if host[0] not in ('work.table1','work.cs3_copy1')]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    conn=pymysql.connect(host='127.0.0.1', port=3306, user='root', password='popeye12.', db='work', )
    cur=conn.cursor()
    cur.execute('''select CONCAT(TABLE_SCHEMA,'.',TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA="work"''')
    res=cur.fetchall()
    asyncio.run(main())
    print(dict(sorted(table_dict.items(),key=lambda item:item[1],reverse=True)))

    # for item in res:
    #     asyncio.get_event_loop().run_until_complete(get_num(item[0]))

