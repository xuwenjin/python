#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#测试select查询

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

rs = cursor.fetchall()
for row in rs:
    print row

cursor.close()
conn.close()