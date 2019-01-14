#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# pandas-排序

import numpy as np, pandas as pd

print "Series排序--"

s1 = pd.Series(np.array(np.random.randint(1, 20, 10)))
print s1
# 按索引排序
print s1.sort_index()
# 按值排序(默认ascending=True，即正序排序)
print s1.sort_values(ascending=False)

print "DataFrame排序--"

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
# 先根据Age排序，再根据Height排序
print student.sort_values(by=['Age', 'Height'])
