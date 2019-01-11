#!/usr/bin/env python
# -*- coding:utf-8 -*-

# pandas-创建序列、数据框

import numpy as np, pandas as pd

arr1 = np.arange(10)
print arr1

# 通过一维数组创建序列
s1 = pd.Series(arr1)
print s1
print type(s1)

# 通过二维数组创建数据框
arr = np.array(np.arange(12)).reshape(4, 3)
print arr
df1 = pd.DataFrame(arr)
print df1
print type(df1)

# 通过字典创建数据框
dic2 = {'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8], 'c': [9, 10, 11, 12], 'd': [13, 14, 15, 16]}
print(dic2)
df2 = pd.DataFrame(dic2)
print df2
dic3 = {'one': {'a': 1, 'b': 2, 'c': 3, 'd': 4}, 'two': {'a': 5, 'b': 6, 'c': 7, 'd': 8},
        'three': {'a': 9, 'b': 10, 'c': 11, 'd': 12}}
print(dic3)
df3 = pd.DataFrame(dic3)
print df3

# 通过数据框创建数据框(可以理解为从数据框中取一个子数据框)
df4 = df3[['one', 'three']]
print df4
df5 = df3['one']
print df5
df6 = df2['b']
print df6
