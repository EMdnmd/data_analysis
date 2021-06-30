'''
模板介绍：
coding: utf-8
Team : 无
Author：张恒瑞
Date ：2021/6/25 8:38
Tool ：PyCharm
'''
import  matplotlib.pyplot  as mp
import  numpy as np
"""
创建两个窗口
"""
#设置窗口名  和 背景填充色
mp.figure("第一个窗口",facecolor="red")
mp.plot([0,1],[1,2])
mp.title("A")
mp.ylabel("time",fontsize=19)
mp.xlabel("price")
mp.tick_params(labelsize=14)
# 设置图像网格样式
mp.grid(linestyle=":")


mp.figure("第二个窗口",facecolor="yellow")
mp.title("B")
mp.ylabel("time",fontsize=19)
mp.xlabel("price")
mp.tick_params(labelsize=10)
# 设置图像网格样式
mp.grid(linestyle="-")
mp.plot([1,2],[2,1])


mp.show()