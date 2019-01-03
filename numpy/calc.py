#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#numpy相关函数测试-数学运算

import numpy as np

a = np.array([[1,2],
             [3,4]])
b = np.array([[5,6],
             [7,7]])
#相加
print a + b
print np.add(a,b)

#相减
print a - b
print np.subtract(a, b)

#相乘
print a * b
print np.multiply(a, b)

#相除
print a/b
print np.divide(a,b)

#算术平方根
print np.sqrt(a)

#sum函数-求一个数组中给定轴上的元素的总和
print np.sum(a)
#计算每列的和(y轴)
print np.sum(a, axis=0)
#计算每行的和(x轴)
print np.sum(a, axis=1)

#mean函数-求一个数组中给定轴上的元素的平均值
print np.mean(a)
#计算每列的平均值(y轴)
print np.mean(a, axis=0)
#计算每行的平均值(x轴)
print np.mean(a, axis=1)

#amin函数-用于计算数组中的元素沿指定轴的最小值
print np.amin(a)
#计算每列的最小值(y轴)
print np.amin(a, axis=0)
#计算每行的最小值(x轴)
print np.amin(a, axis=1)

#amax-用于计算数组中的元素沿指定轴的最大值
print np.amax(a)
#计算每列的最大值(y轴)
print np.amax(a, axis=0)
#计算每行的最大值(x轴)
print np.amax(a, axis=1)