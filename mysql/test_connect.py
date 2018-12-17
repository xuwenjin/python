#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import MySQLdb as mdb

conn = mdb.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='xwj'
)
cursor = conn.cursor()

print conn
print cursor

cursor.close()
conn.close()