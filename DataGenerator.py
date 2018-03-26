#-*- coding:utf-8 -*-
import numpy as np

def generateData(cnt, dims, labels):
    # cnt 代表生成样本的数量
    # dims 第一个参数代表有几个特征向量，之后的dims[0]个数每个代表每一维向量可能取值的个数
    # labels 代表了输出可能取值的个数
    data = np.zeros([cnt, dims[0]])
    for i in range(1, dims[0]+1):
        data[:,i] = np.round(np.random.rand(cnt)*dims[i])
    return data
