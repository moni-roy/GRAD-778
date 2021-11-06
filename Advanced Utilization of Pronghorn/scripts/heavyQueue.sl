#!/bin/bash
#SBATCH --job-name=heavyqueue_job
#SBATCH --output=heavyqueue_job.out
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:03:00
#SBATCH --cpus-per-task=16
#SBATCH --hint=compute_bound
#SBATCH --mem-per-cpu=2GB
#SBATCH --partition=cpu-core-0
#SBATCH --account=cpu-s5-grad_778-1
#SBATCH --mail-user=[yourEMAIL]
#SBATCH --mail-type=ALL

sleep 120
hostname
