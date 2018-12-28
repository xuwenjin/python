#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#numpy相关函数测试-arange

import numpy as np

#arange函数-创建数值范围并返回 ndarray 对象(默认从0开始)
arr = np.arange(3)
print arr

#不包含终止值
arr = np.arange(1,5)
print arr

#从1到10，步长为2
arr = np.arange(1,10,2)
print arr

#多维数组运算
arr = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
#每一行的第1列加10
arr[[0,1,2],[1,1,1]] += 10
print arr
#使用arange
arr[np.arange(3), [1,1,1]] += 10
print arr
arr[np.arange(3), 1] += 10
print arr

#找出大于10的元素
r_index = arr > 10
print r_index
print arr[r_index]
#也可以简化：
print arr[arr > 10]