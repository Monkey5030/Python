# -*- coding: utf-8 -*-
import json
import time

import pymysql, redis
from multiprocessing import Process
from collections import Counter


class redis_func():
    def redis_push(r, key, data):
        pass

        def auto_list_rebuild_def(new_val):
            val = []
            for item in range((len(new_val) // 8) + 1):
                i, s = 0, []
                while i < 8:
                    try:
                        s.append(new_val[(item * 8) + i][0])
                    except:
                        pass
                    i += 1
                val.append(s)
            return val

        def redis_lpush_list(r, key, val):
            i = len(val)
            if i == 8:
                r.lpush(key, val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7])
            elif i == 7:
                r.lpush(key, val[0], val[1], val[2], val[3], val[4], val[5], val[6])
            elif i == 6:
                r.lpush(key, val[0], val[1], val[2], val[3], val[4], val[5])
            elif i == 5:
                r.lpush(key, val[0], val[1], val[2], val[3], val[4])
            elif i == 4:
                r.lpush(key, val[0], val[1], val[2], val[3])
            elif i == 3:
                r.lpush(key, val[0], val[1], val[2])
            elif i == 2:
                r.lpush(key, val[0], val[1])
            elif i == 1:
                r.lpush(key, val[0])
            else:
                pass

        val_list = auto_list_rebuild_def(data)
        i = len(val_list)
        for val in val_list:
            redis_lpush_list(r, key, val)
            i -= 1


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

MYSQL_PIPLINE = {
    "u": "xxx",
    "p": "xxx",
    "h": "xxx",
    "d": "xxx"}


SAVE_MYSQL_PIPLINE = {
    "u": "xxx",
    "p": "xxx",
    "h": "xxx",
    "port": xxx
} 


if __name__ == '__main__':
    db = pymysql.connect(MYSQL_PIPLINE["h"], MYSQL_PIPLINE["u"], MYSQL_PIPLINE["p"], MYSQL_PIPLINE["d"])
    db2 = pymysql.connect(host=SAVE_MYSQL_PIPLINE["h"], user=SAVE_MYSQL_PIPLINE['u'],
                          password=SAVE_MYSQL_PIPLINE['p'], port=SAVE_MYSQL_PIPLINE['port'])
