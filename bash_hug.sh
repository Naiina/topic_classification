#!/bin/bash
#$ -N xhug
#$ -l h_rt=5:10:00
#$ -l h_vmem=80G
#$ -cwd
#$ -q gpu
#$ -pe gpu-a100 1
source ~/.bashrc
conda activate /exports/eddie/scratch/s2523033/anaconda/envs/subj_env/
export NEPTUNE_API_TOKEN="eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vYXBwLm5lcHR1bmUuYWkiLCJhcGlfdXJsIjoiaHR0cHM6Ly9hcHAubmVwdHVuZS5haSIsImFwaV9rZXkiOiI5YzllNjM4MS0zYjBhLTQwNGUtOGM3Mi1hYjE3ZTVjOWVjMTgifQ=="

export NEPTUNE_PROJECT="naiina/topic-classifier-more-epochs"
python hugging_face_utils.py


#python train_classifier.py --out_file loss_early_stop_1 --lr_file l_lr_1.json
#python read_xml.py
#python train_bert_classif.py
conda deactivate

