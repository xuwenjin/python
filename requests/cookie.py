#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#测试cookie相关

import requests

#将cookies发送到服务器
url = 'https://httpbin.org/cookies'
cookies = dict(cookie_are='working')
r = requests.get(url, cookies=cookies)
print r.text


