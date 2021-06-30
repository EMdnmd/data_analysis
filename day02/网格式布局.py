'''
模板介绍：
coding: utf-8
Team : 无
Author：张恒瑞
Date ：2021/6/25 10:53
Tool ：PyCharm
'''
import  matplotlib.pyplot as mp
import  matplotlib.gridspec as mg
# 创建一个窗口

mp.figure("A")

# 设置表格的矩阵模块
gs=mg.GridSpec(3,3)
# 根据需求合并网格
mp.subplot(gs[0,:2])
mp.text(
    0.5,
    0.5,
    "1"
)
mp.xticks([])
mp.yticks([])
mp.subplot(gs[0:2,2:])
mp.text(
    0.5,
    0.5,
    "2"
)
mp.xticks([])
mp.yticks([])
mp.subplot(gs[1:,:1])
mp.text(
    0.5,
    0.5,
    "3"
)
mp.xticks([])
mp.yticks([])
mp.subplot(gs[2:,1:])
mp.text(
    0.5,
    0.5,
    "4"
)
mp.xticks([])
mp.yticks([])
mp.subplot(gs[1:2,1:2])
mp.text(
    0.5,
    0.5,
    "5"
)
mp.xticks([])
mp.yticks([])
mp.show()