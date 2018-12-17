#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#测试python自带的网页下载器：test

import urllib2, cookielib

url = "http://www.baidu.com"

print "第一种方法"
response1 = urllib2.urlopen(url)
#打印状态码
print response1.getcode()
print len(response1.read())

print "第二种方法"
request = urllib2.Request(url)
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print "第三种方法"
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
# print len(response3.read())
print cj
print response3.read()


