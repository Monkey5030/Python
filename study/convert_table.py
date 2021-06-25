# encoding=utf-8
# 作者：Admin
# 日期：2021/6/23 15:55
# 工具：PyCharm
import asyncio
import aiomysql


# nohup python3 convert_table.py >convert.log 2>&1&  6788
class mysql_func():
    def __init__(self,host='127.0.0.1', port=3306, user='root', password='popeye12.',db='work', charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.db = db
        self.charset = charset

    async def get_pool(self):
        '''
        初始化，获取数据库连接池
        '''
        try:
            print("aiomysql.create_pool")
            pool = await aiomysql.create_pool(host='127.0.0.1', port=3306, user='root', password='popeye12.',db='work', charset='utf8')
            return pool
        except asyncio.CancelledError:
            raise asyncio.CancelledError
        except Exception as ex:
            print("mysql数据库连接失败：{}".format(ex.args[0]))
            return False


# async def getCurosr():
#     '''
#     获取db连接和cursor对象，用于db的读写操作
#     '''
#     pool=await get_pool()
#     conn = await pool.acquire()
#     cur = await conn.cursor()
#     return conn, cur


async def execute(begin, end):
    # 网络IO操作：连接MySQL
    # conn = await aiomysql.connect(host='111.186.58.185', port=18086, user='root', password='Boguan@365', db='school_talent_info', )
    # # 网络IO操作：创建CURSOR
    # cur = await conn.cursor()
    # 网络IO操作：执行SQL
    mysql = mysql_func(host='127.0.0.1', port=3306, user='root', password='popeye12.',db='work', charset='utf8')
    pool=await mysql.get_pool()
    conn = await pool.acquire()
    cur = await conn.cursor()
    # pool1=await mysql.get_pool()
    # conn1 = await pool.acquire()
    # cur1 = await conn.cursor()
    try:
        await cur.execute(
            f'''insert ignore into cnblog2 (title,url,summary,postdate,view,comment,digg,source_url,insert_date) 
                select title,url,summary,postdate,view,comment,digg,source_url,insert_date from cnblog 
                where id  between {begin} and {end}''')
        # 网络IO操作：获取SQL结果
        await  conn.commit()
        result = await cur.fetchall()
    except Exception as e:
        print(e)
    # 网络IO操作：关闭链接
    await cur.close()
    conn.close()


if __name__ == '__main__':
    for begin in range(1, 4000, 1):
        end = begin + 100
        # print(begin)
        # asyncio.run(execute(begin, end))
        new_loop=asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        loop=asyncio.get_event_loop()
        task=asyncio.ensure_future(execute(begin,end))
        loop.run_until_complete(asyncio.wait([task]))
        st=task.result()
    print(st)
