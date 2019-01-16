#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import itchat
import requests, json
import random

API_KEY = '59f97d30c1e549fe9e0447a409457b78'
USER_ID = '65ef34878098be1e'


# 给文件传输助手发消息
# itchat.auto_login()
# itchat.send('hello, filhelper', toUserName='filehelper')

# 向图灵机器人发送消息，返回相应的语料
def requestTuling(msg):
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    # post请求-请求参数为json对象
    reqJsonObj = {
        "reqType": 0,
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
    # 返回值为json字符串，转为json对象
    res_json_obj = json.loads(response.text)
    result = res_json_obj['results'][0]
    res_text = result['values']['text']
    return res_text


# 向百度机器人发送消息，返回相应的语料
def requestBaidu(msg):
    access_token = '24.37424cd8daa86a1986e6555e6ad55676.2592000.1550216350.282335-15430898'
    url = 'https://aip.baidubce.com/rpc/2.0/unit/service/chat?access_token={}'.format(access_token)
    # post请求-请求参数为json对象
    reqJsonObj = {
        "version": "2.0",
        "service_id": "S12581",
        "skill_ids": ["31304"],
        "log_id": "1010",
        "session": "1",
        "dialog_state": {
            "contexts": {
                "SYS_REMEMBERED_SKILLS": ["31304"]
            }
        },
        "request": {
            "user_id": "UNIT_DEV_1010",
            "query": msg,
            "query_info": {
                "type": "TEXT"
            }
        }
    }
    response = requests.post(url, data=json.dumps(reqJsonObj))
    # 返回值为json字符串，转为json对象
    res_json_obj = json.loads(response.text)
    # 本轮应答列表
    response_list = res_json_obj['result']['response_list'][0]
    # 动作列表
    action_list = response_list['action_list']
    # 生成一个随机数
    ran_index = random.randint(0, len(action_list) - 1)
    # 取出随机的一个动作
    action = action_list[ran_index]
    res_text = action['say']
    return res_text


# 微信回复功能
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    # 接收别人发给自己的消息
    return requestBaidu(msg.text)


# 自动登录
# itchat.auto_login()
# itchat.run()

# 图灵机器人与百度机器人聊天
def auto_chat(msg):
    text = msg
    print "我："
    for item in range(10):
        text_tuling = requestTuling(text)
        print "图灵机器人：", text_tuling
        text_baidu = requestBaidu(text_tuling)
        print "百度机器人：", text_baidu
        text = text_baidu


auto_chat("你是谁")
