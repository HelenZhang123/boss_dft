#!/bin/bash


rm -f geometry1.in
mkdir calc_folder
mkdir -p data
mv geometry.in calc_folder/geometry.in
cp control.in calc_folder/control.in
mv xyz.xyz calc_folder/xyz.xyz

cd calc_folder

ulimit -s unlimited

export OMP_NUM_THREADS=1

module load FHI-aims/latest-intel-2020.0

#mpirun -n 12 aims | tee output.out
srun aims.200821.scalapack.mpi.x &> output.out
#cp ../testdata.out output.out

E=($(grep 'Total energy correct' output.out  | awk '{ print  $6 }' |tail -n 1))
echo $E > energy.out
cp output.out ../output.out
cp energy.out ../energy.out
cd ..

mv calc_folder data/$i
