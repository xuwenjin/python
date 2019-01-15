#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# pandas-利用pandas实现Excel的数据透视表功能

import numpy as np, pandas as pd

"""
pivot_table(data,values=None,
            index=None,
            columns=None,
            aggfunc='mean',
            fill_value=None,
            margins=False,
            dropna=True,
            margins_name='All')  
data：需要进行数据透视表操作的数据框
values：指定需要聚合的字段
index：指定某些原始变量作为行索引
columns：指定哪些离散的分组变量
aggfunc：指定相应的聚合函数
fill_value：使用一个常数替代缺失值，默认不替换
margins：是否进行行或列的汇总，默认不汇总
dropna：默认所有观测为缺失的列
margins_name：默认行汇总或列汇总的名称为'All'
"""

stu_dic = {
    'Age': [14, 13, 13, 14, 14, 12, 12, 15, 13, 12, 11, 14, 12, 15, 16, 12, 15, 11, 15],
    'Height': [69, 56.5, 65.3, 62.8, 63.5, 57.3, 59.8, 62.5, 62.5, 59, 51.3, 64.3, 56.3, 66.5, 72, 64.8, 67, 57.5,
               66.5],
    'Name': ['Alfred', 'Alice', 'Barbara', 'Carol', 'Henry', 'James', 'Jane', 'Janet', 'Jeffrey', 'John', 'Joyce',
             'Judy', 'Louise', 'Marry', 'Philip', 'Robert', 'Ronald', 'Thomas', 'Willam'],
    'Sex': ['M', 'F', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'F', 'F', 'M', 'M', 'M', 'M', 'M'],
    'Weight': [112.5, 84, 98, 102.5, 102.5, 83, 84.5, 112.5, 84, 99.5, 50.5, 90, 77, 112, 150, 128, 133, 85, 112]
}
student = pd.DataFrame(stu_dic)

# 一个分组变量（Sex），一个数值变量（Height）作统计
table1 = pd.pivot_table(student, values=['Height'], columns=['Sex'])
print table1

# 一个分组变量（Sex），两个数值变量（Height,Weight）作统计汇总
table2 = pd.pivot_table(student, values=['Height', 'Weight'], columns=['Sex'])
print table2

# 两个分组变量（Sex，Age)，两个数值变量（Height,Weight）作统计汇总
table3 = pd.pivot_table(student, values=['Height', 'Weight'], columns=['Sex', 'Age'])
print table3

# 联表形式(将结果进行非堆叠操作（unstack）)
table4 = pd.pivot_table(student, values=['Height', 'Weight'], columns=['Sex', 'Age']).unstack()
print table4

#使用多个聚合函数
table5 = pd.pivot_table(student, values=['Height','Weight'], columns=['Sex'],aggfunc=[np.mean,np.median,np.std])
print table5
