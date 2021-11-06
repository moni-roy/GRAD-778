#!/bin/bash

#SBATCH --job-name=myFirstJob
#SBATCH --output=myOutput.txt
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=100M
#SBATCH --hint=nomultithread
#SBATCH --time=00:01:00
#SBATCH --partition=cpu-core-0
#SBATCH --account=cpu-s5-grad_778-1
#SBATCH --mail-user=YOUREMAILHERE
#SBATCH --mail-type=ALL

module load python3

start=$(date +%s.%N)

for i in $(seq 1 64)
do
    srun --ntasks=1 --nodes=1 --cpus-per-task=1 --exclusive python SquareMyNumber.py $i &
done

wait

end=$(date +%s.%N)    

runtime=$(python -c "print(${end} - ${start})")

echo "Runtime was $runtime"
