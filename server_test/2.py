#测试ase是否可以输出正常的结构
from ase.io import read,write
from ase import Atoms
from ase.constraints import FixAtoms
from ase.build import surface
from ase.calculators.aims import Aims
from ase.build import fcc100, add_adsorbate, bulk, fcc111, fcc110
from ase.visualize import view
import os


atoms = Atoms('CCOHHHHHH',positions=[[-2.389565,0,-0.025097],[-1.12958,0,0.830453],[0,0,0],[-3.2863,0,0.634172],[-2.401584,-0.909258,-0.666871],[-2.401596,0.90881,-0.667506],[-1.117561,0.909258,1.472227],[-1.117549,0.90881,1.472862],[0.754514,0,0.563979]])
slab = fcc110('Al', a=4.041, size=(3,3,4))
constraint_l = FixAtoms(indices=[atom.index for atom in slab if atom.index < 3*3*1])
slab.set_constraint(constraint_l)
add_adsorbate(slab,atoms,3,position=(2,2),mol_index = 2)
slab.center(vacuum=15.0, axis=2)
#view(slab)
write('geometry1.in',slab,format='aims')