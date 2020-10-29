#测试boss是否可以正常优化三元函数

import numpy as np
from boss.bo.bo_main import BOMain

def func(X):
    x = X[0,:]
    #print(x)
    f=x[0]*x[0]+x[1]*x[1]+x[2]*x[2]
    return f

bounds = np.array([[-5., 5.],[-5.,5.],[-5.,5.]])

bo = BOMain(
    func,
    bounds,
    yrange=[0,75 ],
    kernel='rbf',
    initpts=5,
    iterpts=50
)

res = bo.run()