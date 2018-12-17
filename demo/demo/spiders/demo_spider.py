#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import scrapy

#引入容器
from demo.items import DemoItem

"""
创建一个Spider，您必须继承 scrapy.Spider 类， 且定义以下三个属性:
name: 用于区别Spider。 该名字必须是唯一的
start_urls: 包含了Spider在启动时进行爬取的url列表
parse(): 被调用时，每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。 该方法负责解
         析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象
"""
class DemoSpider(scrapy.Spider):

    # 设置爬虫名称
    name = "demo"

    #允许访问的域
    allowed_domains = ["imooc.com"]

    #爬取地址
    start_urls = ["http://www.imooc.com/course/list"]

    #爬取方法(解析response)
    def parse(self, response):
        # 实例一个容器保存爬取的信息
        item = DemoItem()

        base_url = "http://www.imooc.com"
        for box in response.xpath("//div[@class='course-card-container']"):
            #选取a标签的href属性
            item['url'] = base_url + box.xpath('//a/@href').extract()[0]

            #选取h3标签中，class属性为course-card-name的值
            item['title'] = box.xpath('.//h3[@class="course-card-name"]/text()').extract()[0].strip()

            item['img_url'] = "http" + box.xpath('.//img/@src').extract()[0]

            item['description'] = box.xpath('.//p[@class="course-card-desc"]/text()').extract()[0].strip()

            #选取第2个span标签中的值
            item['student']= box.css('span:nth-child(2)::text').extract()[0].strip()

            # 返回信息(不加这个，pipeline中process_item方法将获取不到值)
            yield item



