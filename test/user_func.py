###############################################
'''
2020.10.28
userfunction
duhl
coding=utf-8
python 3.8.5
'''
###############################################
import numpy as np
from ase.io import read,write
from ase import Atoms
from ase.constraints import FixAtoms
from ase.build import surface
from ase.calculators.aims import Aims
from ase.build import fcc100, add_adsorbate, bulk, fcc111, fcc110
from ase.visualize import view
import os


def func(x):

    '''
    从文件读取计数"i"
    '''

    icount = open("i.txt", "r",encoding='utf-8')
    i=int(icount.readline())
    icount.close()
    iplus = open("i.txt", "w",encoding='utf-8')
    i=i+1
    iplus.write(str(i))
    iplus.close()

    wdata = open("data.txt", "a",encoding='utf-8')
    wdata.write(str(i)+"\n"+ str(x)+"\n")


    '''
    基于boss的请求，由ase生成晶体
    '''
    #print(i)
    X=x[0,:]
    #print(X)
    atoms = Atoms('CCOHHHHHH',positions=[[-2.389565,0,-0.025097],[-1.12958,0,0.830453],[0,0,0],[-3.2863,0,0.634172],[-2.401584,-0.909258,-0.666871],[-2.401596,0.90881,-0.667506],[-1.117561,0.909258,1.472227],[-1.117549,0.90881,1.472862],[0.754514,0,0.563979]])
    slab = fcc110('Al', a=4.041, size=(3,3,4))
    constraint_l = FixAtoms(indices=[atom.index for atom in slab if atom.index < 3*3*1])
    slab.set_constraint(constraint_l)
    add_adsorbate(slab,atoms,X[2],position=(X[0],X[1]),mol_index = 2)
    slab.center(vacuum=15.0, axis=2)
    #view(slab)
    write('geometry1.in',slab,format='aims')
    wdata.write("aims finished\n")


    '''
    固定乙醇的O原子
    '''
    infile = open("geometry1.in", "r",encoding='utf-8')
    outfile = open("geometry.in", "w",encoding='utf-8')
    for line in infile:
        outfile.write(line.replace(' O\n', ' O\n\t constrain_relaxation .true.\n'))
    infile.close()
    outfile.close()
    wdata.write("geometry.in finished\n")


    '''
    交由bush脚本提交作业并在out文件中提取能量
    '''
    os.environ['i'] = str(i)
    os.system("./calc.sh")

    wdata = open("data.txt", "a",encoding='utf-8')
    wdata.write("calc.sh finished\n")
    efinf = open('energy.out',"r",encoding='utf-8')
    E = float(efinf.readline())
    efinf.close()
    wdata.close()
    os.system("rm -f energy.out")

    return E
