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
