#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# matplotlib数据可视化-简单画图

from matplotlib import pyplot as plt

plt.plot([1, 2, 3], [4, 5, 1])
# 在画布上显示
plt.show()

x = [5, 2, 7]
y = [2, 16, 4]
plt.plot(x, y)
# 图片的标题
plt.title('Image Title')
# 坐标轴Y轴
plt.ylabel('Y axis')
# 坐标轴X轴
plt.xlabel('X axis')
plt.show()
