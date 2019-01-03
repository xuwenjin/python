#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#numpy相关函数测试

import numpy as np

a = np.array([[1,2],
             [3,4]])

#tile函数-在指定的行和列上重复元素
print np.tile(a, (1,2))
print np.tile(a, (2,1))


a = np.array([[2,4,1,6],
              [5,2,7,3]])
#argssort函数-对指定行或列进行排序(返回下标)
print a.argsort()
print a.argsort(axis=0)

#矩阵转置-行转列
print a.T
print np.transpose(a)