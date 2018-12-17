#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#图片下载

import requests

def download_img():
    # url = "http://img3.imgtn.bdimg.com/it/u=2316988767,4179839980&fm=26&gp=0.jpg"
    url = "http://img0.imgtn.bdimg.com/it/u=3266433975,3113381467&fm=26&gp=0.jpg"
    #伪造headers信息
    headers = {'Referer': 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=github'}
    #stream=True,使用流进行传输
    response = requests.get(url, headers=headers, stream=True)
    print response.status_code, response.reason
    with open('demo.jpg', 'wb') as fd:
        #iter_content(128), 128位处理相应内容
        for chunk in response.iter_content(128):
            fd.write(chunk)

download_img()