#!/bin/bash
#SBATCH -o FHIjob%j.out
##SBATCH --constraint=[opt]
#SBATCH -N 2 
#SBATCH -n 48
#SBATCH -p short
#SBATCH -o ./test.out.%j
#SBATCH -e ./test.err.%j
#SBATCH --time=04:00:00 --mem-per-cpu=4096
#SBATCH --exclusive


ulimit -s unlimited


module load ASE/3.15.0-foss-2017b-Python-3.6.3
module load Python/3.6.3-foss-2017b


module load FHI-aims/latest-OpenMPI-intel-2020.0-scalapack


srun python start.py
