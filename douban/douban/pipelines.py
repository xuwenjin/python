# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from elasticsearch import Elasticsearch
from douban.settings import es_host, es_port

class DoubanPipeline(object):

    def __init__(self):
        self.index = "xwj"  #es索引
        self.type = "douban_movie" #es文档类型
        self.client = Elasticsearch([{'host':es_host, 'port':es_port}])

    def process_item(self, item, spider):
        data = dict(item)
        #数据保存到es
        self.client.index(index=self.index, doc_type=self.type, body=data)
        return item
