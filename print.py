import numpy as np
from ase.io import read,write
from ase import Atoms
from ase.constraints import FixAtoms
from ase.build import surface
from ase.calculators.aims import Aims
from ase.build import fcc100, add_adsorbate, bulk, fcc111, fcc110
from ase.visualize import view
import os

X=[5.4253315149E+00,5.2031571641E+00,3.6440891188E+00]
#print(X)


atoms = Atoms('OHCHHCHHH',positions=[[0.0000000000,0.0000000000,0.0000000000],[-0.3399169000,0.6879265600,0.5768999600],[1.4199650400,-0.0864104400,0.1453702500],[1.6850596700,-1.0670213400,0.4815652800],[1.8874004500,0.1057950300,-0.7977422600], [1.8948619700,0.9552466200,1.1754301900],[2.9573533100,0.8905894500,1.2842033700],[1.6297667300,1.9358573600,0.8392351900],[1.4274265500,0.7630414400,2.1185427600]])
slab = fcc110('Al', a=4.041, size=(3,3,4))
constraint_l = FixAtoms(indices=[atom.index for atom in slab if atom.index < 3*3*1])
slab.set_constraint(constraint_l)
add_adsorbate(slab,atoms,X[2],position=(X[0],X[1]),mol_index = 2)
slab.center(vacuum=15.0, axis=2)
view(slab)
write('geometry1.in',slab,format='aims')




infile = open("geometry1.in", "r",encoding='utf-8')
outfile = open("geometry.in", "w",encoding='utf-8')
for line in infile:
    outfile.write(line.replace(' O\n', ' O\n\t constrain_relaxation .true.\n'))
infile.close()
outfile.close()

os.system("rm -f geometry1.in")
