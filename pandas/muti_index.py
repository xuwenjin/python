#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# pandas-多层索引的使用

import numpy as np, pandas as pd

s = pd.Series(np.arange(1,10), index=[["a","a","a","b","b","c","c","d","d"],[1,2,3,1,2,3,1,2,3]])
print s
print s.index

#选取外层索引为a的数据
print s['a']
#选取外层索引为a和内层索引为1的数据
print s['a',1]
#选取外层索引为a和内层索引为1,3的数据
print s['a'][[1,3]]
#层次化索引的切片，包括右端的索引
print s[['a','c']]
print s['b':'d']
#通过unstack方法可以将Series变成一个DataFrame
#数据的类型以及数据的输出结构都变成了DataFrame，对于不存在的位置使用NaN填充
print s.unstack()