#测试python是否可以正常调用sh脚本

import os

os.system("rm -rf 4/")

os.system("./4_1.sh")

for i in range(0,10):
    os.environ['i'] = str(i)
    os.system("./4_2.sh")
