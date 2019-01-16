#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# pandas实践——2012美国总统竞选赞助数据分析

# %matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
各字段含义
cand_nm – 接受捐赠的候选人姓名
contbr_nm – 捐赠人姓名
contbr_st – 捐赠人所在州
contbr_employer – 捐赠人所在公司
contbr_occupation – 捐赠人职业
contb_receipt_amt – 捐赠数额（美元）
contb_receipt_dt – 收到捐款的日期
"""

# 读取文本数据，返回值类型为DataFrame
data_01 = pd.read_csv('data_01.csv')
data_02 = pd.read_csv('data_02.csv')
data_03 = pd.read_csv('data_03.csv')

# 数据合并(列合并)
data = pd.concat([data_01, data_02, data_03])
# print data

# 数据分析
print data.head(10)

# 查看数据的信息，包括每个字段的名称、非空数量、字段的数据类型
print data.info()

# 用统计学指标快速描述数据的概要
print data.describe()

# 从data.info()得知，contbr_employer、contbr_occupation均有少量缺失值,均填充为NOT PROVIDED
data['contbr_employer'].fillna('NO PROVIDED', inplace=True)
data['contbr_occupation'].fillna('NO PROVIDED', inplace=True)
print data.info()

# 数据转换
# 查看数据中总统候选人都有谁
print "有{}位候选人，分别是：".format(len(data['cand_nm'].unique()))
print data['cand_nm'].unique()

# 通过搜索引擎等途径，获取到每个总统候选人的所属党派，建立字典parties，候选人名字作为键，所属党派作为对应的值
# Republican：共和党  Democrat：民主党
parties = {'Bachmann, Michelle': 'Republican',
           'Cain, Herman': 'Republican',
           'Gingrich, Newt': 'Republican',
           'Huntsman, Jon': 'Republican',
           'Johnson, Gary Earl': 'Republican',
           'McCotter, Thaddeus G': 'Republican',
           'Obama, Barack': 'Democrat',
           'Paul, Ron': 'Republican',
           'Pawlenty, Timothy': 'Republican',
           'Perry, Rick': 'Republican',
           "Roemer, Charles E. 'Buddy' III": 'Republican',
           'Romney, Mitt': 'Republican',
           'Santorum, Rick': 'Republican'}

# 通过map映射函数，增加一列party存储党派信息
print data['cand_nm'].map(parties)
data['party'] = data['cand_nm'].map(parties)

print "查看两个党派赞助次数的情况:"
# value_counts()：以Series形式返回指定列的不同取值的频率
print data['party'].value_counts()

print "查看两个党派赞助总金额的情况:"
print data.groupby('party').sum()

print "按照职业汇总对赞助总金额进行排序:"
print data.groupby('contbr_occupation')['contb_receipt_amt'].sum().sort_values(ascending=False)[:20]

print "赞助金额筛选"
print "限定数据集只有正出资额:"
data = data[data['contb_receipt_amt'] > 0]

print "按照候选人分类对赞助总金额进行排序:"
print data.groupby('cand_nm')['contb_receipt_amt'].sum().sort_values(ascending=False)

# 选取候选人为Obama、Romney的子集数据:
# isin()接受一个列表，判断该列中元素是否在列表中
data_vs = data[data['cand_nm'].isin(['Obama, Barack', 'Romney, Mitt'])].copy()

print "面元化数据:"
# cut函数：将数据进行离散化、将连续变量进行分段汇总
bins = np.array([0, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000])
labels = pd.cut(data_vs['contb_receipt_amt'].head(20), bins)
print labels

print "通过pivot_table根据党派和职业对数据进行聚合，然后过滤掉总出资不足200万美元的数据:"
# 按照党派、职业对赞助金额进行汇总，类似excel中的透视表操作，聚合函数为sum
by_occupation = pd.pivot_table(data,
                               values=['contb_receipt_amt'],
                               index=['contbr_occupation'],
                               columns=['party'],
                               aggfunc=['sum'])
over_2mm = by_occupation[by_occupation.sum(1) > 2000000]
print over_2mm

# 绘制条状图
over_2mm.plot(kind='bar')
plt.show()
