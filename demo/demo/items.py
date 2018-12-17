# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

"""
Item 是保存爬取到的数据的容器；其使用方法和python字典类似， 并且提供了额外保
护机制来避免拼写错误导致的未定义字段错误
"""

import scrapy

class DemoItem(scrapy.Item):

    #课程标题
    title = scrapy.Field()

    #课程url
    url = scrapy.Field()

    #课程标题图片
    img_url = scrapy.Field()

    #课程描述
    description = scrapy.Field()

    #学习人数
    student = scrapy.Field()




