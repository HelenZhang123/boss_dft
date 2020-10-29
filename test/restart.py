###############################################
'''
2020.10.28
restart
duhl
coding=utf-8
python 3.8.5
基于之前的数据进行更多次迭代的贝叶斯优化
'''
###############################################
import numpy as np
from boss.bo.bo_main import BOMain
from user_func import func
import os


bounds = np.array([[3.0,6.0],[3.0,6.0],[1.0,3.0]])


bo = BOMain.from_file('boss.rst', f=func, iterpts=50)
res = bo.run()