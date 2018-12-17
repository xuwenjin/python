#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#测试requests中的get请求、post请求

import requests, json

#get请求
r = requests.get('https://api.github.com/events')
print r.status_code
#状态码200的常量
print r.status_code == requests.codes.ok
print r.text
print r.content
#将response对象转为json格式
print r.json()

#post请求
r = requests.post('https://httpbin.org/post', data = {'key':'value'})
print r.status_code, r.text

#将请求参数拼接到url后面，例如：url?key1=value1&key2=value2
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print r.url   #https://httpbin.org/get?key2=value2&key1=value1

#在请求中增加请求头
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent':'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print r.text

#请求参数dict类型转为json字符串
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
#直接使用json参数也可以：
r = requests.post(url, json=payload)

#测试404
bad_r = requests.get('https://httpbin.org/status/404')
print bad_r.status_code
#使用raise_for_status()可以打印出错误日志。如果状态码是200，这个将返回None
print bad_r.raise_for_status()
