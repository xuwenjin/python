#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#把github的图片全部爬下来

import requests, re

"""
爬取分析：
打开百度图片网页，会先发送一个acjson?tn=resultjson&ipn=…的请求。页面向下滚动时，也会发送该请求，只是查询条件会不一样
请求中，有以下几个关键字段：
    word: 查询词条
    rn：每页图片数量(默认30条)
    pn：当前显示的图片数量(30的倍数)
每次请求，会返回一个data，其包该页查询的图片集合信息。其中的thumbURL字段表示该图片的路径
"""

#keyword：关键词  count：爬取几页
def getImgDatas(keyword, count):
    base_url = r"http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word={word}&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&selected_tags=&cg=star&pn={pn}&rn=30&gsm=1e&1544844426775="
    #将中文转为utf-8编码
    # keyword = urllib.parse.quote(keyword, "utf-8")
    #所有的图片信息
    dataList = []
    for i in range(30, 30*count+30, 30):
        url = base_url.format(word=keyword, pn=str(i))
        print "url:", url
        #每次发送请求的返回值：每个图片的信息
        data = requests.get(url).json().get('data')
        print "单次请求data:", data
        dataList.append(data)
    return dataList

#通过图片集合信息，将数据爬取到本地
def getImg(dataList):
    for pindex, data in enumerate(dataList):
        pcount = str(pindex + 1)
        print '第%s页图片：' % pcount
        for index, item in enumerate(data):
            try:
                url = item.get('thumbURL')
                if url is None:
                    print '图片链接不存在：%s' % url
                    continue
                headers = {"Referer": "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8"}
                #一定得加headers，不然爬取的图片打不开
                response = requests.get(url, timeout=15, headers=headers, stream=True)
                count = pcount + "_" + str(index + 1)
                imgName = count + '.jpg'
                # open('imgs2/' + imgName, 'wb').write(response.content)
                with open('imgs2/' + imgName, 'wb') as fd:
                    for chunk in response.iter_content(128):
                        fd.write(chunk)
                print "成功下载第%s张图片 %s" % (count, str(url))
            except Exception as e:
                print "下载第%s张图片失败， %s" % (count, str(url))
                print e
                continue

if __name__ == '__main__':
    dataList = getImgDatas("陈道明", 3)
    print "所有图片信息：", dataList
    getImg(dataList)
