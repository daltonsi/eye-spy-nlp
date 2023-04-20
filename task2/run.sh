#!/bin/bash
# The interpreter used to execute the script

#"#SBATCH" directives that convey submission options:

#SBATCH --job-name=task2-LHS712
#SBATCH --mail-user=daltonsi@umich.com
#SBATCH --mail-type=BEGIN,END
#SBATCH --nodes=1
#SBATCH --time=5:00:00
#SBATCH --account=vgvinodv0
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --gpus-per-task=1
#SBATCH --cpus-per-gpu=1
#SBATCH --mem-per-gpu=5000m
#SBATCH --output=/home/%u/model_results/task2-LHS712/%x-%j.log
#SBATCH --error=/home/%u/model_results/Ttask2-LHS712/%x-%j.err

# The application(s) to execute along with its input arguments and options:

~/anaconda3/envs/eye-nlp-env-env/bin/python train_and_test.py  $@