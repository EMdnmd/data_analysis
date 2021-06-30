'''
模板介绍：
coding: utf-8
Team : 无
Author：张恒瑞
Date ：2021/6/18 10:52
Tool ：PyCharm
'''
from random import randint

import matplotlib.pyplot as pl
import  numpy as   np
x=np.linspace(-np.pi,np.pi ,100)
y1=np.sin(x)
y2=np.cos(x)
#设置
pl.plot(x,y1,label=r'$y=sin(x)$')
pl.plot(x,y2,label=r'$y=cos(x)$')
vals=[-np.pi,-np.pi/2,0,np.pi/2,np.pi]
text=[r"$\pi$",r"$-\frac{\pi}{2}$","0",r"$\frac{\pi}{2}$","∏"]
# 设置坐标系
ax=pl.gca()
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")
ax.spines["left"].set_position(('data',0))
ax.spines["bottom"].set_position(('data',0))
print(r"$\pi$")
# 设置标签
# 设置特殊点
px=[np.pi/2,np.pi/2]
py=[1,0]
pl.scatter(px,py,marker="o",s=20,color="red",label="x y")
# 设置备注
pl.annotate("adada",#设置备注
            xycoords="data",#备注目标点所使用的坐标系
            xy=(np.pi/2,1),
            textcoords="offset  points",
            xytext=(50,30),
            fontsize=14,
            arrowprops=dict(
                arrowstyle="->",
                connectionstyle="angle3"
            )
)
pl.legend()
pl.show()

