#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# matplotlib数据可视化(导入样式包，改变线条宽度或颜色)

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')
x = [5, 8, 10]
y = [12, 16, 6]
x2 = [6, 9, 11]
y2 = [6, 15, 7]
plt.plot(x, y, 'g', label='line one', linewidth=5)
plt.plot(x2, y2, 'r', label='line two', linewidth=5)
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

# 设置图例位置
plt.legend()
# 网格
plt.grid(True, color='k')
plt.show()
