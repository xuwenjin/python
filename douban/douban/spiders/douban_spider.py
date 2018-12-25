# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

#爬取豆瓣

class DoubanSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250/']

    def parse(self, response):
        #循环电影的条目
        movie_list = response.xpath("//div[@class='article']/ol[@class='grid_view']/li")
        for selector in movie_list:
            #导入Item文件
            douban_item = DoubanItem()
            # 序号
            douban_item['serial_number'] = selector.xpath(".//div[@class='pic']/em/text()").extract_first()
            # 电影名称
            douban_item['movie_name'] = selector.xpath(".//div[@class='hd']/a/span[1]/text()").extract_first()
            # 电影介绍
            content = selector.xpath(".//div[@class='bd']/p/text()").extract()
            content_s = ""
            for i_content in content:
                content_s += "".join(i_content.split())
            douban_item['introduce'] = content_s
            # 星级
            douban_item['star'] = selector.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract_first()
            # 电影评论数
            douban_item['evalute'] = selector.xpath(".//div[@class='star']/span[last()]/text()").extract_first()
            # 电影描述
            douban_item['describe'] = selector.xpath(".//p[@class='quote']/span[@class='inq']/text()").extract_first()

            #将数据yield到pipelines
            yield  douban_item

        #解析下一页，取的后页的xpath
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            link = next_link[0]
            yield scrapy.Request("http://movie.douban.com/top250" + link, callback=self.parse)