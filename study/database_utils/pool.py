# encoding=utf-8
# 作者：Admin
# 日期：2021/7/6 10:06
# 工具：PyCharm
import datetime

import pymysql
from dbutils.pooled_db import PooledDB


class mysql_func(object):
    __pool = None;

    def __init__(self, mincached=10, maxcached=20, maxshared=10, maxconnections=200, blocking=True, maxusage=100,
                 setsession=None, reset=True,
                 host='localhost', user='root', passwd='xxxxxxxx', port=3306, db='work', charset='utf8mb4'):
        if not self.__pool:
            self.__class__.__pool = PooledDB(pymysql,
                                             mincached, maxcached,
                                             maxshared, maxconnections, blocking,
                                             maxusage, setsession, reset,
                                             host=host, port=port, db=db,
                                             user=user, passwd=passwd,
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
            if isinstance(result_dict,dict):
                result_replace = {k: v.__str__() for k, v in result_dict.items() if isinstance(v, datetime.datetime)}
                result_dict.update(result_replace)
            if isinstance(result_dict,tuple):
                tuple_info=list()
                for item in result_dict:
                    if isinstance(item,datetime.datetime):
                        tuple_info.append(item.__str__())
                    else:
                        tuple_info.append(item)
                result_dict=tuple(tuple_info)
        return result_dict

    def get_data(self, sql):
        self._cursor.execute(sql)
        data = self._cursor.fetchall()
        data=[self.__dict_datetime_obj_to_str(item) for item in data]
        return data
        # 存数据，int类型返回成功条数

    def get_row_number(self, sql, data=None):
        if data is None or len(data) == 0:
            self._cursor.execute(sql)
        else:
            if type(data[0]) != type([]):
                data = [data]
            self._cursor.executemany(sql, data)
        data = self.curors.rowcount
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
        self._conn.autocommit(0)

    def end(self, option='commit'):
        """结束事务"""
        if option == 'commit':
            self._conn.autocommit()
        else:
            self._conn.rollback()


if __name__ == "__main__":
    mc = mysql_func()
    sql1 = 'SELECT * from cnblog where id>10 and id<20'
    result1 = mc.get_json(sql1)
    # result1 = mc.get_data(sql1)
    print(result1)

