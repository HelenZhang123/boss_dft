import numpy as np
from ase.io import read,write
from ase import Atoms
from ase.constraints import FixAtoms
from ase.build import surface
from ase.calculators.aims import Aims
from ase.build import fcc100, add_adsorbate, bulk, fcc111, fcc110
from ase.visualize import view
import os
import math

X=[8,4,2,60,90,180]
#print(X)



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



def f(X):


    os.system("python3 gc.py -zmat zmat.zmat")

    xyzcount = len(open("xyz.xyz",'r').readlines())
    xyz = open("xyz.xyz","r")
    posi=[]
    ii=0
    posi = np.zeros((xyzcount, 3))
    rd_x = X[3]
    rd_y = X[4]
    rd_z = X[5]

    for line in xyz:
        x = line.split()
        if len(x)==4:
            x0 = float(x[1])
            y0 = float(x[2])
            z0 = float(x[3])
            (x1,y1,z1)=rotate_x_axis(x0,y0,z0,rd_x)
            (x2,y2,z2)=rotate_y_axis(x1,y1,z1,rd_y)
            (x3,y3,z3)=rotate_z_axis(x2,y2,z2,rd_z)
            posi[ii][0] = x3
            posi[ii][1] = y3
            posi[ii][2] = z3
            ii = ii+1
    xyz.close()
    #print(posi)

    '''
    基于boss的请求，由ase生成晶体
    '''

    atoms = Atoms('OHCHHCHHH',positions=posi)
    slab = fcc110('Al', a=4.041, size=(3,3,4))
    constraint_l = FixAtoms(indices=[atom.index for atom in slab if atom.index < 3*3*1])
    slab.set_constraint(constraint_l)
    add_adsorbate(slab,atoms,X[2],position=(X[0],X[1]),mol_index = 2)
    slab.center(vacuum=15.0, axis=2)
    #view(slab)
    write('geometry.in',slab,format='aims')


os.system("VESTA geometry.in")

if __name__ == '__main__':
    f(X)
