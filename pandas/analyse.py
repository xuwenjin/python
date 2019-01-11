#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 利用pandas的DataFrames进行统计分析

import numpy as np, pandas as pd

# 确定随机数生成器的种子
np.random.seed(1234)
d1 = pd.Series(2 * np.random.normal(size=100) + 3)

print '非空元素计算: ', d1.count()  # 非空元素计算
print '最小值: ', d1.min()  # 最小值
print '最大值: ', d1.max()  # 最大值
print '最小值的位置: ', d1.idxmin()  # 最小值的位置，类似于R中的which.min函数
print '最大值的位置: ', d1.idxmax()  # 最大值的位置，类似于R中的which.max函数
print '10%分位数: ', d1.quantile(0.1)  # 10%分位数
print '求和: ', d1.sum()  # 求和
print '均值: ', d1.mean()  # 均值
print '中位数: ', d1.median()  # 中位数
print '众数: ', d1.mode()  # 众数
print '方差: ', d1.var()  # 方差
print '标准差: ', d1.std()  # 标准差
print '平均绝对偏差: ', d1.mad()  # 平均绝对偏差
print '偏度: ', d1.skew()  # 偏度
print '峰度: ', d1.kurt()  # 峰度
print '描述性统计指标: ', d1.describe()  # 一次性输出多个描述性统计指标


# 必须注意的是，descirbe方法只能针对序列或数据框，一维数组是没有这个方法的
# 这里自定义一个函数，将这些统计描述指标全部汇总到一起:
def stats(x):
    return pd.Series([x.count(), x.min(), x.idxmin(), x.quantile(.25), x.median(), x.quantile(.75),
                      x.mean(), x.max(), x.idxmax(), x.mad(), x.var(), x.std(), x.skew(), x.kurt()],
                     index=['Count', 'Min', 'Whicn_Min', 'Q1', 'Median', 'Q3', 'Mean', 'Max',
                            'Which_Max', 'Mad', 'Var', 'Std', 'Skew', 'Kurt'])


print(stats(d1))
