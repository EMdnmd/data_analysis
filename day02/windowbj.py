'''
模板介绍：
coding: utf-8
Team : 无
Author：张恒瑞
Date ：2021/6/25 10:35
Tool ：PyCharm
'''

import  matplotlib.pyplot as mp
mp.figure("填充窗口",facecolor="red")
# 创建一个3*3的九宫格 在第一个画图
# 第一个框
mp.subplot(3,3,1)
mp.plot([0,1],[1,2])
mp.subplot(3,3,2)
#第二个框
mp.plot([0,1],[1,2])
# 第三个框
mp.subplot(3,3,3)
# 设置一个文本
mp.text(
    0.5, 0.5, #位置
    "1",#文本
    ha="center",
    va="center",
    size=36,
    alpha=0.6 #透明度
)
# 干掉刻度值
mp.xticks([])
mp.yticks([])
mp.show()