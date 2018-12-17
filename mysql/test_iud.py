#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#测试新增、修改、删除

import MySQLdb as mdb

conn = mdb.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='xwj'
)
cursor = conn.cursor()

sql_insert = "insert into user(id, age) values(7, 100)"
sql_update = "update user set age = 30 where id = 7"
sql_delete = "delete from user where id <=3"
try:
    cursor.execute(sql_insert)
    print cursor.rowcount
    cursor.execute(sql_update)
    print cursor.rowcount
    cursor.execute(sql_delete)
    print cursor.rowcount

    #事物提交
    conn.commit()
except Exception as e:
    print e
    #事物回滚
    conn.rollback()

cursor.close()
conn.close()