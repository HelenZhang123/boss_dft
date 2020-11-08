import  numpy as np
import  math


def rotate_z_axis(x,y,z,radio_z):
    new_x = x*math.cos(math.radians(radio_z))-y*math.sin(math.radians(radio_z))
    new_y = x*math.sin(math.radians(radio_z))+y*math.cos(math.radians(radio_z))
    new_z = z
    return new_x, new_y, new_z

def rotate_x_axis(x,y,z,radio_x):
    new_x = x
    new_y = y*math.cos(math.radians(radio_x))-z*math.sin(math.radians(radio_x))
    new_z = y*math.sin(math.radians(radio_x))+z*math.cos(math.radians(radio_x))
    return new_x,new_y,new_z

def rotate_y_axis(x,y,z,radio_y):
    new_x = z*math.sin(math.radians(radio_y))+x*math.cos(math.radians(radio_y))
    new_y = y
    new_z = z*math.cos(math.radians(radio_y))-x*math.sin(math.radians(radio_y))
    return new_x,new_y,new_z

#沿z轴将向量(1,0,0)逆时针旋转30°
x1,y1,z1=rotate_z_axis(1,0,0,30)
print(x1,y1,z1)

