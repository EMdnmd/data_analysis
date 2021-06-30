'''
模板介绍：
coding: utf-8
Team : 无
Author：张恒瑞
Date ：2021/6/16 9:14
Tool ：PyCharm
'''

import  numpy as np

# arrays=np.arange(0,100)
# arrays.shape=(10,10)
# arrays.astype("float32")
# print(arrays.dtype)
#


data=[
    ("zs",[1,2,3],12),
    ("ls",[1,22,31],19),
    ("lb",[12,12,44],10)
    ]
# s=np.array(data,dtype="U2 ,3int64,int64")
# print(s)
# nps=np.arange(0,20)
# a=nps.reshape(2,10)
# print(a)
# b=a.reshape(5,2,2)
# print(b)
# nps[0]=123
# c=b.reshape(10,2)
# print(c)
# d=c.ravel()#变为一维数组
# print(d)
# nps=np.arange(0,100)
# npa=nps.reshape(10,10)
# tf=[True,False,True,
#     False,True,False,
#     False,False,True]
#
# print(npa[(npa%3==0) & (npa%7==0) ])

# a=["苹果","华为","三星","小米","oppo"]
#
# sk=np.array(a)
# l=[1,0,3,2,4]
#
# print(sk
# from  PIL import  Image
# # 导入图片
# file=Image.open("mongodbfor循环.png")
# # 生成图片narray数组怕
# sk=np.array(file)
# # 竖向切割
# s=np.hsplit(sk,2)
# # 生成图片
# im=Image.fromarray(s[0])
# im.save("a.png")