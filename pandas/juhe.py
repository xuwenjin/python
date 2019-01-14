#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# pandas-对数据聚合、排序和多表连接操作

import numpy as np, pandas as pd

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

# 根据性别分组，计算各组别中学生身高和体重的平均值：
print student.groupby('Sex').mean()

# 如果不对原始数据作限制的话，聚合函数会自动选择数值型数据进行聚合计算。如果不想对年龄计算平均值的话，就需要剔除改变量：
print student.drop(['Age'], axis=1).groupby('Sex').mean()

# groupby还可以使用多个分组变量，例如根本年龄和性别分组，计算身高与体重的平均值：
print student.groupby(['Sex', 'Age']).mean()

# 对每个分组计算多个统计量(平均值，中位数)：
print student.drop(['Age'], axis=1).groupby(['Sex']).agg([np.mean, np.median])
