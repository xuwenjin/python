#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import itchat
import requests, json

API_KEY = '59f97d30c1e549fe9e0447a409457b78'
USER_ID = '65ef34878098be1e'

#给文件传输助手发消息
# itchat.auto_login()
# itchat.send('hello, filhelper', toUserName='filehelper')

#向图灵机器人发送消息，返回相应的语料
def requestTL(msg):
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    #post请求-请求参数为json对象
    reqJsonObj = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": msg
            },
        },
        "userInfo": {
            "apiKey": API_KEY,
            "userId": USER_ID
        }
    }
    response = requests.post(url, data=json.dumps(reqJsonObj))
    #返回值为json字符串，转为json对象
    resJsonObj = json.loads(response.text)
    result = resJsonObj['results'][0]
    resText = result['values']['text']
    print resText
    return resText

#微信回复功能
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    #接收别人发给自己的消息
    return requestTL(msg.text)

#自动登录
itchat.auto_login()
itchat.run()