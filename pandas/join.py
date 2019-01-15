#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# pandas-内连接、左连接

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

dic2 = {'Name': ['Alfred', 'Alice', 'Barbara', 'Carol', 'Henry', 'Jeffrey', 'Judy', 'Philip', 'Robert', 'Willam'],
        'Score': [88, 76, 89, 67, 79, 90, 92, 86, 73, 77]}
score = pd.DataFrame(dic2)

# 现在想把学生表student与学生成绩表score做一个关联(默认内连接)
print pd.merge(student, score, on="Name")
# 左连接(给how赋值)
print pd.merge(student, score, on="Name", how="left")


