# encoding=utf-8
# 作者：Admin
# 日期：2021/6/23 15:55
# 工具：PyCharm
import asyncio
import aiomysql


# nohup python3 convert_table.py >convert.log 2>&1&  6788

async def execute(begin,end):
    # 网络IO操作：连接MySQL
    conn = await aiomysql.connect(host='111.186.58.185', port=18086, user='root', password='Boguan@365', db='school_talent_info', )
    # 网络IO操作：创建CURSOR
    cur = await conn.cursor()
    # 网络IO操作：执行SQL
    try:
        await cur.execute(f'''insert ignore into talent_info_2 (name,school,school_url,academy,academy_url,list_url,institute,department,professional,header_img,email,phone,research_direction,subject,work_experience,representative_work,
                          award,project,teach,supervise_stutent,social_appointments,flag,mainurl,content,unit) 
                          SELECT name,school,school_url,academy,academy_url,list_url,institute,department,professional,header_img,email,phone,
                          research_direction,subject,work_experience,
                          representative_work,award,project,teach,supervise_stutent,social_appointments,flag,mainurl,content,unit 
                          FROM talent_info_1 where id  between {begin} and {end}''')
        # 网络IO操作：获取SQL结果
        await  conn.commit()
        result = await cur.fetchall()
    except Exception as e:
        print(e)
    # 网络IO操作：关闭链接
    await cur.close()
    conn.close()

if __name__ == '__main__':
    for begin in range(2555395,2700000,1000):
        end=begin+999
        # print(begin)
        asyncio.run(execute(begin,end))
        # asyncio.get_event_loop().run_until_complete(execute(begin,end))