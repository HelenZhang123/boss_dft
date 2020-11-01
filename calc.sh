#!/bin/bash

outfile="energy.out"

rm -f geometry1.in
mkdir calc_folder
mkdir -p data
mv geometry.in calc_folder/geometry.in
cp control.in calc_folder/control.in

cd calc_folder
ulimit -s unlimited
module load FHI-aims/latest-OpenMPI-intel-2020.0-scalapack
srun aims.200821.scalapack.mpi.x &> output.out
#cp ../testdata.out output.out

E=($(grep 'Total energy correct' output.out  | awk '{ print  $6 }' |tail -n 1))
echo $E > $outfile
cp $outfile ../$outfile
cd ..

mv calc_folder data/$i
