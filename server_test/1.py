#测试系统文件io及其顺序
import os

os.system("rm -r 1.txt")

for i in range(0,10):
    wdata = open("1.txt", "a",encoding='utf-8')
    #print(i)
    wdata.write(str(i)+"\n========================\n\n")
    wdata.close()