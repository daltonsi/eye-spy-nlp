import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.data.dataset import random_split
import torch.utils.data as data

from transformers import AutoTokenizer, AutoModelForSequenceClassification, \
    TrainingArguments, Trainer

from datasets import load_dataset


import pandas as pd
import numpy as np
import os
import time

DATA_PATH = '/home/daltonsi/eye-spy-nlp/source_data/task2_source.csv'
UNIQUE_LABELS = ["ALLERGIES", "ANESTHESIA", "COMPLICATIONS", "DIAGNOSIS", "HISTORY", "MEDICATION","OBJECTIVE","OTHER","PLAN","PROCEDURE","SUBJECTIVE"]

# Train Parameters
lr = 1e-2
batch_size = 16
run_name = "LHS712-task2"
num_epochs = 1
logging_steps = 5000
save_total_limit = 1
seed = 1
out_dir = '/home/daltonsi/eye-spy-nlp/task2/output'
model_name = 'bert-base-cased'
resume_from_checkpoint = False


def tokenize_data(df):
    tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')

    return tokenizer(df['text'], padding='max_length', truncation=True)


def preprocess(df):
    # tweets = df['Tweet']
    # tod = df['TimeOfDay']
    df['tokens'] = df.apply(tokenize_data, axis=1)
    return df

def transform_labels(label):

    label = label['label']
    num = 0
    if label == 'ALLERGIES':
        num = 0
    elif label == 'ANESTHESIA':
        num = 1
    elif label == 'COMPLICATIONS':
        num = 2
    elif label == 'DIAGNOSIS':
        num = 3
    elif label == 'HISTORY':
        num = 4
    elif label == 'MEDICATION':
        num = 5
    elif label == 'OBJECTIVE':
        num = 6
    elif label == 'OTHER':
        num = 7
    elif label == 'PLAN':
        num = 8
    elif label == 'PROCEDURE':
        num = 9
    elif label == 'SUBJECTIVE':
        num = 10
    return {'labels': num}


def main():
    task2_df = pd.read_csv(DATA_PATH,header=0,usecols=['label','text']).dropna()
    task2_df.reset_index().to_csv('task2_full_data.csv')
    dataset = load_dataset('csv', data_files={'train': 'task2_full_data.csv'}, split='train')




    remove_columns = ['index', 'Unnamed: 0','label']

    tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')

    def tokenize_data(df):
        return tokenizer(df['text'], padding='max_length', truncation=True)

    dataset = dataset.map(tokenize_data, batched=True)
    dataset = dataset.map(transform_labels, remove_columns=remove_columns)



    training_args = TrainingArguments("test_trainer", num_train_epochs=3, logging_steps=100)

    model = AutoModelForSequenceClassification.from_pretrained('bert-base-cased', num_labels=11)
    train_dataset = dataset.shuffle(seed=10).select(range(237))
    eval_dataset = dataset.shuffle(seed=10).select(range(237, 339))

    trainer = Trainer(
        model=model, args=training_args, train_dataset=train_dataset, eval_dataset=eval_dataset
    )
    trainer.train()


    return None





if __name__ == '__main__':
    main()