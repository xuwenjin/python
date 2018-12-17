#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#事件钩子

import requests

def get_key_info(response, *args, **kw):
    print "事件回调"
    print response.headers['Content-type']


def main():
    requests.get("https://www.baidu.com", hooks=dict(response=get_key_info))

main()