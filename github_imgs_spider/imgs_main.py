#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#把github的图片全部爬下来

import requests
import re

"""
爬取分析：
查看百度图片网站源代码，会发现很多objURL数据，这些就是页面上图片的url。
请求这些url，即可爬取这些图片
如下的做法，只爬取了第一页(默认30个图片)的数据
"""

def downloadImg(imgUrls):
    """给出图片链接，下载所有图片"""
    for index, url in enumerate(imgUrls):
        try:
            response = requests.get(url, timeout=15)
            count = str(index + 1)
            imgName = count + '.jpg'
            with open('imgs/' + imgName, 'wb') as fd:
                for chunk in response.iter_content(128):
                    fd.write(chunk)
                print "成功下载第%s张图片 %s" % (count, str(url))
        except Exception as e:
            print "下载第%s张图片失败， %s" % (count, str(url))
            print e
            continue

if __name__ == '__main__':
    root_url = r'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=陈道明'
    response = requests.get(root_url)
    if response.status_code == requests.codes.ok:
        # 解决中文乱码
        response.content.decode('gbk', 'ignore')
        #(.*?) 非贪婪模式，也就是说只匹配符合条件的最少字符
        #re.S 使 . 匹配包括换行在内的所有字符
        imgUrls = re.findall('"objURL":"(.*?)",', response.content, re.S)
        print "所有链接：", imgUrls
        downloadImg(list(set(imgUrls)))





