#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#pandas-查询

import numpy as np, pandas as pd

stu_dic = {
    'Age':[14,13,13,14,14,12,12,15,13,12,11,14,12,15,16,12,15,11,15],
    'Height':[69,56.5,65.3,62.8,63.5,57.3,59.8,62.5,62.5,59,51.3,64.3,56.3,66.5,72,64.8,67,57.5,66.5],
    'Name':['Alfred','Alice','Barbara','Carol','Henry','James','Jane','Janet','Jeffrey','John','Joyce','Judy','Louise','Marry','Philip','Robert','Ronald','Thomas','Willam'],
    'Sex':['M','F','F','F','M','M','F','F','M','M','F','F','F','F','M','M','M','M','M'],
    'Weight':[112.5,84,98,102.5,102.5,83,84.5,112.5,84,99.5,50.5,90,77,112,150,128,133,85,112]
}
student = pd.DataFrame(stu_dic)

#查询数据的前n行。不传默认为前5行
print student.head()
print student.head(3)

#查询数据的末尾n行。不传默认为末尾5行
print student.tail()
print student.tail(2)

#查询指定的行(行索引)
print '----查询指定行----'
#单行时，只需要一个[]，此时类型变成Series
print student.loc[1]
print type(student.loc[1])
#多行时，必须使用两个[]
print student.loc[[0,1,4,5]]
print type(student.loc[[0,1,4,5]])

#查询指定的列
print '----查询指定列----'
#单列时，只需要一个[]，此时类型变成Series
print student['Age']
print type(student['Age'])
#多列时，必须使用两个[]
print student[['Age', 'Name', 'Sex']]
print student[['Age', 'Name', 'Sex']].head(2)

#如果是多个条件的查询，必须在&（且）或者|（或）的两端条件用括号括起来。
#查询出所有12岁以上的女生信息
print student[(student['Age'] > 12) & (student['Sex'] == 'F')]

#查询出所有12岁以上的女生姓名、身高和体重
print student[(student['Age'] > 12) & (student['Sex'] == 'F')][['Name','Height', 'Weight']]

