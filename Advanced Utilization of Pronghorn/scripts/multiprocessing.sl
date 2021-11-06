#!/bin/bash

#SBATCH --job-name=myParallelJob
#SBATCH --output=myOutput.txt
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=1000M
#SBATCH --hint=nomultithread
#SBATCH --time=00:01:00
#SBATCH --partition=cpu-core-0
#SBATCH --account=cpu-s5-grad_778-1
#SBATCH --mail-user=YOUREMAILHERE
#SBATCH --mail-type=ALL

module load python3

srun python AddSquaresMultiThreadingMany.py
