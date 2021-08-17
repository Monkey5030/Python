dbutils_func.py
# encoding=utf-8
# 作者：Admin
# 日期：2021/7/6 10:06
# 工具：PyCharm
import datetime
import json

import pymysql
from dbutils.pooled_db import PooledDB


class mysql_func(object):
    __pool = None;

    def __init__(self, mincached=10, maxcached=20, maxshared=10, maxconnections=200, blocking=True, maxusage=100,
                 setsession=None, reset=True,
                 host='localhost', user='root', password='popeye12.', port=3306, database='work', charset='utf8mb4'):
        """
        :param mincached:连接池中空闲连接的初始数量
        :param maxcached:连接池中空闲连接的最大数量
        :param maxshared:共享连接的最大数量
        :param maxconnections:创建连接池的最大数量
        :param blocking:超过最大连接数量时候的表现，为True等待连接数量下降，为false直接报错处理
        :param maxusage:单个连接的最大重复使用次数
        :param setsession:optional list of SQL commands that may serve to prepare
            the session, e.g. ["set datestyle to ...", "set time zone ..."]
        :param reset:how connections should be reset when returned to the pool
            (False or None to rollback transcations started with begin(),
            True to always issue a rollback for safety's sake)
        :param host:数据库ip地址
        :param port:数据库端口
        :param db:库名
        :param user:用户名
        :param passwd:密码
        :param charset:字符编码
        """
        if not self.__pool:
            self.__class__.__pool = PooledDB(pymysql,
                                             mincached, maxcached,
                                             maxshared, maxconnections, blocking,
                                             maxusage, setsession, reset,
                                             host=host, port=port, database=database,
                                             user=user, password=password,
                                             charset=charset,
                                             # cursorclass=pymysql.cursors.DictCursor
                                             )
        self._conn = None
        self._cursor = None
        self.__get_conn()

    def __get_conn(self):
        self._conn = self.__pool.connection();
        self._cursor = self._conn.cursor();

    def close(self):
        try:
            self._cursor.close()
            self._conn.close()
        except Exception as e:
            print(e)

        # 取数据，tuple类型返回

    @staticmethod
    def __dict_datetime_obj_to_str(result_dict):
        """把字典里面的datatime对象转成字符串，使json转换不出错"""
        if result_dict:
            if isinstance(result_dict, dict):
                result_replace = {k: v.__str__() for k, v in result_dict.items() if
                                  isinstance(v, datetime.datetime) | isinstance(v, datetime.date)}
                result_dict.update(result_replace)
            if isinstance(result_dict, tuple):
                tuple_info = list()
                for item in result_dict:
                    if isinstance(item, datetime.datetime) | isinstance(item, datetime.date):
                        tuple_info.append(item.__str__())
                    else:
                        tuple_info.append(item)
                result_dict = tuple(tuple_info)
        return result_dict

    def get_data(self, sql):
        self._cursor.execute(sql)
        data = self._cursor.fetchall()
        data = [self.__dict_datetime_obj_to_str(item) for item in data]
        return data
        # 存数据，int类型返回成功条数

    def get_row_number(self, sql, data=None):
        self.begin()
        if data is None or len(data) == 0:
            self._cursor.execute(sql)
        else:
            # if type(data[0]) != type([]):
            #     data = [data]
            self._cursor.executemany(sql, data)
        data = self._cursor.rowcount
        self.end()
        return data
        # 取数据，[dict]类型返回

    #
    def get_json(self, sql):
        self._cursor.execute(sql)
        columns = [col[0] for col in self._cursor.description]
        data = [dict(zip(columns, row)) for row in self._cursor.fetchall()]
        data = [self.__dict_datetime_obj_to_str(item) for item in data]
        return data

    def begin(self):
        """开启事务"""
        self._conn.commit()


    def end(self, option='commit'):
        """结束事务"""
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()


class MysqlClient(object):
    __pool = None;

    def __init__(self, mincached=10, maxcached=20, maxshared=10, maxconnections=200, blocking=True,
                 maxusage=100, setsession=None, reset=True,
                 host='127.0.0.1', port=3306, database='mysql',
                 user='root', password='popeye12.', charset='utf8mb4'):
        """

        :param mincached:连接池中空闲连接的初始数量
        :param maxcached:连接池中空闲连接的最大数量
        :param maxshared:共享连接的最大数量
        :param maxconnections:创建连接池的最大数量
        :param blocking:超过最大连接数量时候的表现，为True等待连接数量下降，为false直接报错处理
        :param maxusage:单个连接的最大重复使用次数
        :param setsession:optional list of SQL commands that may serve to prepare
            the session, e.g. ["set datestyle to ...", "set time zone ..."]
        :param reset:how connections should be reset when returned to the pool
            (False or None to rollback transcations started with begin(),
            True to always issue a rollback for safety's sake)
        :param host:数据库ip地址
        :param port:数据库端口
        :param db:库名
        :param user:用户名
        :param passwd:密码
        :param charset:字符编码
        """

        if not self.__pool:
            self.__class__.__pool = PooledDB(pymysql,
                                             mincached, maxcached,
                                             maxshared, maxconnections, blocking,
                                             maxusage, setsession, reset,
                                             host=host, port=port, database=database,
                                             user=user, password=password,
                                             charset=charset,
                                             cursorclass=pymysql.cursors.DictCursor
                                             )
        self._conn = None
        self._cursor = None
        self.__get_conn()

    def __get_conn(self):
        self._conn = self.__pool.connection();
        self._cursor = self._conn.cursor();

    def close(self):
        try:
            self._cursor.close()
            self._conn.close()
        except Exception as e:
            print(e)

    def __execute(self, sql, param=()):
        count = self._cursor.execute(sql, param)
        return count

    @staticmethod
    def __dict_datetime_obj_to_str(result_dict):
        """把字典里面的datatime对象转成字符串，使json转换不出错"""
        if result_dict:
            result_replace = {k: v.__str__() for k, v in result_dict.items() if
                              isinstance(v, datetime.datetime) | isinstance(v, datetime.date)}
            result_dict.update(result_replace)
        return result_dict

    def select_one(self, sql, param=()):
        """查询单个结果"""
        count = self.__execute(sql, param)
        result = self._cursor.fetchone()
        """:type result:dict"""
        result = self.__dict_datetime_obj_to_str(result)
        return count, result

    def select_many(self, sql, param=()):
        """
        查询多个结果
        :param sql: qsl语句
        :param param: sql参数
        :return: 结果数量和查询结果集
        """
        count = self.__execute(sql, param)
        result = self._cursor.fetchall()
        """:type result:list"""
        [self.__dict_datetime_obj_to_str(row_dict) for row_dict in result]
        return count, result

    def execute(self, sql, param=()):
        count = self.__execute(sql, param)
        return count

    def begin(self):
        """开启事务"""
        self._conn.autocommit(0)

    def end(self, option='commit'):
        """结束事务"""
        if option == 'commit':
            self._conn.autocommit()
        else:
            self._conn.rollback()


if __name__ == "__main__":
    mc = mysql_func(host='127.0.0.1')
    sql1 = 'SELECT * from cnblog where id>10 and id<20'
    result1 = mc.get_json(sql1)
    # result1 = mc.get_data(sql1)
    print(result1)

    # mc = MysqlClient(host='127.0.0.1',user='root',database='work')
    # sql1 = 'SELECT * from cnblog where id=1000'
    # result1 = mc.select_one(sql1)
    # print(json.dumps(result1[1], ensure_ascii=False))
    # sql2 = 'SELECT * FROM cnblog  WHERE  id IN (%s,%s,%s)'
    # param = (2, 3, 4)
    # print(json.dumps(mc.select_many(sql2, param)[1], ensure_ascii=False))

```
# 从别的py引用此代码为
```
import sys
sys.path.append(absolutepath')
from dbutils_func import mysql_func,MysqlClient

mysql=mysql_func()
print(mysql.get_json('select current_date() as date'))

mysql1=MysqlClient()
print(mysql1.select_one('select current_date() as date'))

```
