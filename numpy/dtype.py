#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#numpy相关函数测试-dtype

import numpy as np

#dtype 数据类型

#int32
arr = np.array([1,2])
print arr.dtype

#float64
arr = np.array([1.1, 2])
print arr.dtype
arr = np.array([1.1, 1.2])
print arr.dtype

#float转整形
arr = np.array([1.1, 1.2], dtype=np.int32)
print arr
print arr.dtype
