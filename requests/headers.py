#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#测试headers相关

import requests

r = requests.get('https://httpbin.org/cookies')
headers = r.headers
print headers
#heanders不区分大小写
print headers['Content-type']
print headers.get('content-type')

