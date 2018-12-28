#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#numpy相关函数测试

import numpy as np

arr = np.array([1,2,3])
print arr
print type(arr)
#数组维度，返回一个元组 (行数, 列数)
print arr.shape

arr2 = np.array([1,2,3,4,5,6])
print arr2
print arr2.shape
#不改变数据的条件下修改形状。-1表示占位符，自动计算出值
arr2 = arr2.reshape(2,-1)
print arr2
print arr2.shape
#不改变数据的条件下修改形状
arr2 = arr2.reshape(-1,2)
print arr2
print arr2.shape
#取数组值
print arr2[2,0]

#zeros函数-创建指定大小的数组，数组元素以 0 来填充
# 默认为浮点数
arr = np.zeros(3)
print arr
# 设置类型为整数
arr = np.zeros((5,), dtype = np.int)
print arr
#多维数组
arr = np.zeros((3,3))
print arr

#ones函数-创建指定形状的数组，数组元素以 1 来填充：
arr = np.ones((2,3))
print arr

#full函数-创建指定形状的数组，以指定元素来填充
arr = np.full((3,3), 0)
print arr
arr = np.full((2,3), 1)
print arr

#eye函数-函数返回一个矩阵，对角线元素为 1，其他位置为零
arr = np.eye(3, 3)
print arr

#random函数-创建一个随机矩阵，每个元素值是0-1之间
arr = np.random.random((4,3))
print arr

#索引
arr = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
#取多维数组的值
print arr[0], arr[1], arr[2] #取每行值
print arr[0, 1], arr[1, 2], arr[2, 0] #取单个点的值
print arr[:, 0], arr[:, 1], arr[:, 2] #取每列值
print arr[1:, 1:3] #取第1行开始的，第1、2列值




