#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# pandas-利用pandas进行缺失值的处理

import numpy as np, pandas as pd

s1 = pd.Series(np.array([89, 76, None, 45, None, 30]))
print s1
# 查询缺失值个数
print pd.isnull(s1)
print sum(pd.isnull(s1))
# 删除缺失值
print s1.dropna()

stu_dic = {
    'Age': [14, np.nan, np.nan, 12, 13],
    'Height': [69, np.nan, 65.3, 62.8, np.nan],
    'Sex': ['M', np.nan, 'F', 'F', 'M'],
    'Name': ['Alfred', np.nan, 'Barbara', 'Carol', 'Henry'],
}
student = pd.DataFrame(stu_dic)
print student
# 删除缺失值(数据中只要含有缺失值NaN,该数据行就会被删除)
print student.dropna()
# 删除缺失值(使用how="all"，表示只有当整行都缺失时，才删除)
print student.dropna(how="all")

# 用0填补所有缺失值
print "用0填补所有缺失值："
print student.fillna(0)

# 采用前项填充(使用前一行的值)
print "前项填充："
print student.fillna(method="ffill")
print student.ffill()

# 采用后项填充(使用后一行的值)
print "后项填充："
print student.fillna(method="bfill")
print student.bfill()

# 使用常量填充不同的列
print "使用常量填充不同的列:"
print student.fillna({'Age': 20, 'Height': 30.2, 'Sex': 'M', 'Name': 'Xwj'})

age_median = student['Age'].median()
height_mean = student['Height'].mean()
print student.fillna({'Age': age_median, 'Height': height_mean})
