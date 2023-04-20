import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.data.dataset import random_split
import torch.utils.data as data

from transformers import BertTokenizer, BertForSequenceClassification

import pandas as pd
import numpy as np
import os
import time

DATA_PATH = '/home/daltonsi/eye-spy-nlp/source_data/task2_source.csv'

# Train Parameters
lr = 1e-2
epoch = 5
batch_size = 16


class SentenceDataset(data.Dataset):

    def __init__(self, database):
        self.database = database

    def __len__(self):
        return self.database.shape[0]
        #return 128

    def __getitem__(self, idx):
        # return the sentence
        i = self.database["text"][idx]

        # return the label array
        label = self.database.loc[idx, ["ALLERGIES", "ANESTHESIA", "COMPLICATIONS", "DIAGNOSIS", "HISTORY", "MEDICATION","OBJECTIVE","OTHER","PLAN","PROCEDURE","SUBJECTIVE"]]
        label = np.array(label, dtype=float)

        return i, label

def prepare_dataset(data_path: str):
    task2_df = pd.read_csv(data_path,header=0,usecols=['label','text'])
    df = task2_df.set_index('text').dropna(axis=1, how='all')
    df = pd.get_dummies(df, prefix='', prefix_sep='').groupby(level=0, axis=1).max().reset_index()
    dataset = SentenceDataset(df)
    return dataset






def main():

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    dataset = prepare_dataset(DATA_PATH)
    print("Total: %i" % len(dataset))


    return None





if __name__ == '__main__':
    main()