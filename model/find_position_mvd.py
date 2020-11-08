import numpy as np
import math

def rotate_z_axis(x,y,z,radio_z):
    new_x = x*math.cos(math.radians(radio_z))-y*math.sin(math.radians(radio_z))
    new_y = x*math.sin(math.radians(radio_z))+y*math.cos(math.radians(radio_z))
    new_z = z
    #print(new_x,new_y,new_z)
    return new_x, new_y, new_z

def rotate_x_axis(x,y,z,radio_x):
    new_x = x
    new_y = y*math.cos(math.radians(radio_x))-z*math.sin(math.radians(radio_x))
    new_z = y*math.sin(math.radians(radio_x))+z*math.cos(math.radians(radio_x))
    #print(new_x,new_y,new_z)
    return new_x,new_y,new_z

def rotate_y_axis(x,y,z,radio_y):
    new_x = z*math.sin(math.radians(radio_y))+x*math.cos(math.radians(radio_y))
    new_y = y
    new_z = z*math.cos(math.radians(radio_y))-x*math.sin(math.radians(radio_y))
    #print(new_x,new_y,new_z)
    return new_x,new_y,new_z


xyzcount = len(open("xyz.xyz",'r').readlines())
xyz = open("xyz.xyz","r")
posi=[]
i=0
posi = np.zeros((xyzcount, 3))


rd_x = 0
rd_y = 0
rd_z = 30

for line in xyz:
    x = line.split()
    if len(x)==4:
        x0 = float(x[1])
        y0 = float(x[2])
        z0 = float(x[3])
        (x1,y1,z1)=rotate_x_axis(x0,y0,z0,rd_x)
        (x2,y2,z2)=rotate_y_axis(x1,y1,z1,rd_y)
        (x3,y3,z3)=rotate_z_axis(x2,y2,z2,rd_z)
        posi[i][0] = x3
        posi[i][1] = y3
        posi[i][2] = z3
        i = i+1

xyz.close()
print(posi)
