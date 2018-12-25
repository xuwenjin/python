# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import sys

#Unicode的编码问题，读取文件时使用的编码默认是ascii而不是utf8，所以报错。得加上以下代码：
reload(sys)
sys.setdefaultencoding('utf-8')

"""
Pipeline经常进行以下一些操作： 
    清理HTML数据 
    验证爬取的数据(检查item包含某些字段) 
    查重(并丢弃) 
    将爬取结果保存到数据库中
"""

class DemoPipeline(object):

    def __init__(self):
        # 打开文件
        self.file = open('data.csv', 'w')

    # 该方法用于处理数据
    def process_item(self, item, spider):
        # 读取item中的数据
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        print "line:", line
        # 写入文件
        self.file.write(line)
        return item

    # 该方法在spider被开启时被调用。
    def open_spider(self, spider):
        pass

    # 该方法在spider被关闭时被调用。
    def close_spider(self, spider):
        pass
