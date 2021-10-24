#!/bin/bash

#SBATCH --job-name=myMultiprocessingJob5
#SBATCH --output=myMultiprocessingJob_output_5.txt
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=5
#SBATCH --mem-per-cpu=10M
#SBATCH --hint=nomultithread
#SBATCH --time=00:01:00
#SBATCH --partition=cpu-core-0
#SBATCH --account=cpu-s5-grad_778-1
#SBATCH --mail-user=ADDYOUREMAILHERE
#SBATCH --mail-type=ALL

module load python3

srun python AddSquaresMultiThreading.py
