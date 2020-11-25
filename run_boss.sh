#!/bin/bash
#SBATCH -o FHIjob%j.out
##SBATCH --constraint=[opt]
#SBATCH -N 4 
#SBATCH -n 96
#SBATCH -p batch
#SBATCH -o ./test.out.%j
#SBATCH -e ./test.err.%j
#SBATCH --time=72:00:00 --mem-per-cpu=4096
#SBATCH --exclusive


#ulimit -s unlimited

source ~/.bashrc

#export OMP_NUM_THREADS=1

module load ASE/3.15.0-foss-2017b-Python-3.6.3
module load Python/3.6.3-foss-2017b
#module load FHI-aims/latest-intel-2020.0

#boss o boss.in
boss op boss.rst
#boss op boss_mod.rst
