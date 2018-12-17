#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#权限认证

import requests

BASE_URL = 'https://api.github.com'

#在BASE_URL后面拼接请求，以'/'连接
def construct_url(end_point):
    return '/'.join([BASE_URL, end_point])

def basic_auth():
    print "基本认证"
    response = requests.get(construct_url('user'), auth=('imoocdemo', 'imoocdemo123'))
    print response.text
    print response.request.headers

def basic_oauth2():
    print "oauth2认证"
    #从https://github.com/settings/tokens上生成的token
    headers = {"Authorization": "token 1bb029607ecff65fd8c8bb4c324d632a992ec11e"}
    response = requests.get(construct_url('user/emails'), headers=headers)
    print response.status_code
    print response.text
    print response.request.headers

#自定义验证
from requests.auth import AuthBase

#身份验证实现是子类AuthBase。只需要实现其call方法即可
class MyAuth(AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__ (self, req):
        #requests加headers
        req.headers['Authorization'] = ' '.join(['token', self.token])
        return req

#使用AuthBase对象认证
def oauth2():
    auth = MyAuth('1bb029607ecff65fd8c8bb4c324d632a992ec11e')
    response = requests.get(construct_url('user/emails'), auth=auth)
    print response.status_code
    print response.text
    print response.request.headers

oauth2()