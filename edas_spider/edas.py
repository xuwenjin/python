#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#edas服务查询与批量删除

import requests
import sys

#Unicode的编码问题，读取文件时使用的编码默认是ascii而不是utf8，所以报错。得加上以下代码：
reload(sys)
sys.setdefaultencoding('utf-8')

#获取edas服务列表
def getEdasList(url):
    response = requests.get(url)
    print response.status_code, response.reason
    dataList = response.json().get('data').get('result')
    return dataList

#edas服务批量删除
def removeService(url, dataList):
    if dataList is None:
        return
    removeCount = 0
    for data in dataList:
        serviceName = data['dataId']
        payload = {"dataId": serviceName, "group":"HSF", "method":"removeConfig", "srcIp":"10.7.133.197"}
        response = requests.post(url, data=payload)
        try:
            if response.status_code == requests.codes.ok:
                print "成功删除服务：%s" % serviceName
                removeCount = removeCount + 1
        except:
            print "删除服务%s失败" % serviceName
            continue
    print "共删除服务个数：%s" % removeCount


if __name__ == '__main__':
    #查询服务url
    query_url = r"http://localhost:8080/config-center/admin.do?__preventCache=1544858865615&currentPage=1&dataId=&group=&method=listConfig&pageSize=20&srcIp="
    edasList = getEdasList(query_url)
    print "edas服务数量：", len(edasList)
    #删除服务url
    remove_url = r"http://localhost:8080/config-center/admin.do"
    removeService(remove_url, edasList)
