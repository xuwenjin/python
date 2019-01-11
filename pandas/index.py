#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# pandas-索引

import numpy as np, pandas as pd

# 序列索引
s1 = pd.Series(np.array([1, 3, 4, 7, 8, 9]))
print s1
# 如果不给序列一个指定的索引值，则序列自动生成一个从0开始的自增索引。可以通过index查看序列的索引：
print s1.index
# 设定索引
s1.index = ['a', 'b', 'c', 'd', 'e', 'f']
print s1
# 索引
print s1[1], s1['b']
print s1[[1, 3]]
print s1[['a', 'b', 'c']]
print s1[:4]
print s1['b':]
# 如果通过索引标签获取数据的话，末端标签所对应的值是可以返回的
print s1['b':'e']

# 自动化对齐
# 如果有两个序列，需要对这两个序列进行算术运算，这时索引的存在就体现的它的价值了—自动化对齐
s5 = pd.Series(np.array([10, 15, 20, 30, 55, 80]), index=['a', 'b', 'c', 'd', 'e', 'f'])
print(s5)

s6 = pd.Series(np.array([12, 11, 13, 15, 14, 16]), index=['a', 'c', 'g', 'b', 'd', 'f'])
print(s6)
print(s5 + s6)
print(s5 / s6)
# 由于s5中没有对应的g索引，s6中没有对应的e索引，所以数据的运算会产生两个缺失值NaN。注意，这里
# 的算术结果就实现了两个序列索引的自动对齐，而非简单的将两个序列加总或相除。对于数据框的对齐，
# 不仅仅是行索引的自动对齐，同时也会自动对齐列索引（变量名）
