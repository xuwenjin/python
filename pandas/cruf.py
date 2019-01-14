#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# pandas-对数据增删改查

import pandas as pd

stu_dic = {
    'Age': [14, 13, 13, 14, 14, 12, 12, 15, 13, 12, 11, 14, 12, 15, 16, 12, 15, 11, 15],
    'Height': [69, 56.5, 65.3, 62.8, 63.5, 57.3, 59.8, 62.5, 62.5, 59, 51.3, 64.3, 56.3, 66.5, 72, 64.8, 67, 57.5,
               66.5],
    'Name': ['Alfred', 'Alice', 'Barbara', 'Carol', 'Henry', 'James', 'Jane', 'Janet', 'Jeffrey', 'John', 'Joyce',
             'Judy', 'Louise', 'Marry', 'Philip', 'Robert', 'Ronald', 'Thomas', 'Willam'],
    'Sex': ['M', 'F', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'F', 'F', 'M', 'M', 'M', 'M', 'M'],
    'Weight': [112.5, 84, 98, 102.5, 102.5, 83, 84.5, 112.5, 84, 99.5, 50.5, 90, 77, 112, 150, 128, 133, 85, 112]
}
student1 = pd.DataFrame(stu_dic)
print student1

stu_dic2 = {'Name': ['LiuShunxiang', 'Zhangshan'],
            'Sex': ['M', 'F'], 'Age': [27, 23],
            'Height': [165.7, 167.2],
            'Weight': [61, 63]
            }
student2 = pd.DataFrame(stu_dic2)
print student2

print "--新增--"

# 添加新行(concat函数可以自动对齐两个数据框的变量)
student3 = pd.concat([student1, student2])
print student3

# 添加新列(对于新增的列没有赋值，就会出现空NaN的形式)
print pd.DataFrame(student2, columns=['Age', 'Name', 'Height', 'Sex', 'Weight', 'Score'])

print "--删除--"

# 删除数据框(通过del命令实现，该命令可以删除Python的所有对象)
del student2
# print student2

# 删除指定的行(没有改变原数据)
print student1.drop([0, 2, 3])
print "student1:"
print student1

# 根据布尔索引删除行数据，其实这个删除就是保留删除条件的反面数据，例如删除所有14岁以下的学生:
print student1[student1['Age'] > 14]

# 删除列(需要制定axis=1)
print student1.drop(['Height', 'Weight'], axis=1).head()

print "--修改--"
# 将student1中的，Alice的年龄改为99
# 修改得使用 .loc[row_indexer, col_indexer] = value
print student1.loc[student1['Name'] == 'Alice']
student1.loc[student1['Name'] == 'Alice', 'Age'] = 99
print student1[student1['Name'] == 'Alice'][['Name', 'Age']]
