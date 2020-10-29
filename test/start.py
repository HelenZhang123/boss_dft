###############################################
'''
2020.10.28
start
duhl
coding=utf-8
python 3.8.5
第一次开始使用boss优化
'''
###############################################

import numpy as np
from boss.bo.bo_main import BOMain
from user_func import func
import os

os.system("rm -rf i.txt data/ boss.out boss.rst geometry.in geometry1.in data.txt")
wdata = open("data.txt", "a",encoding='utf-8')
wdata.write("delete old files!\n")
wdata.close()


istart = open("i.txt", "w+",encoding='utf-8')
istart.write("0")
istart.close()
os.system("mkdir data")

bounds = np.array([[3.0,6.0],[3.0,6.0],[1.0,3.0]])

wdata = open("data.txt", "a",encoding='utf-8')
wdata.write("================================\nboss start!\n\n===============================\n")
wdata.close()

bo = BOMain(
    func,
    bounds,
    yrange=[-10, 10],
    kernel='stdp',
    initpts=5,
    iterpts=30
)
res = bo.run()