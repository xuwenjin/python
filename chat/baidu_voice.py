#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests, json
import base64, os
from audio import recording

RECORD_FILE = r'./output.wav'


# 获取token
def get_token():
    grant_type = "client_credentials"
    # API Key
    client_id = "2Xd3ytsZT3ZC6FojCFhdYZN0"
    # Secret Key
    client_secret = "cBA6ipfkzoIwPDfk5Xgd6Gr7ozUdw3pW"

    # 拼url
    url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=%s&client_id=%s&client_secret=%s" % (
        grant_type, client_id, client_secret)
    # 获取token
    res = requests.post(url)
    token = json.loads(res.text)["access_token"]
    return token


# 百度-将语音转为文字
def voice_to_word(token):
    url = 'https://vop.baidu.com/server_api'
    headers = {'Content-Type': 'application/json'}

    # 以字节格式读取文件之后进行编码
    with open(RECORD_FILE, "rb") as f:
        speech = base64.b64encode(f.read()).decode('utf-8')
    # 获取文件字节数
    size = os.path.getsize(RECORD_FILE)

    # post请求-请求参数为json对象
    req_json_obj = {
        "format": "wav",
        "rate": "16000",
        "dev_pid": "1536",
        "channel": "1",
        "cuid": "1010",
        "token": token,
        "len": size,
        "speech": speech
    }
    response = requests.post(url, data=json.dumps(req_json_obj), headers=headers)
    # 返回值为json字符串，转为json对象
    res_json_obj = json.loads(response.text)
    res_text = res_json_obj["result"][0]
    return res_text


if __name__ == '__main__':
    # 录音
    recording.record_voice()
    # 获取token
    token = get_token()
    try:
        # 语音识别，返回文字
        ret = voice_to_word(token)
        print ret
    except Exception as e:
        print '失败了'
        print e
