#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#使用post上传文件

import requests

url = 'https://httpbin.org/post'
files = {'file': open('file.txt', 'rb')}
r = requests.post(url, files=files)
print r.text