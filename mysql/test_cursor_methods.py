#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#测试cursor方法

import MySQLdb as mdb

conn = mdb.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='xwj'
)
cursor = conn.cursor()

sql = "select * from user"
cursor.execute(sql)

print cursor.rowcount

rs = cursor.fetchone()
print rs

rs = cursor.fetchmany(3)
print rs

rs = cursor.fetchall()
print rs

cursor.close()
conn.close()