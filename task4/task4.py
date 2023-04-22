import pandas as pd
import re

def clean_data(filepath:str):
    df = pd.read_csv(filepath)
    df.head()
    df['text'] = df['text'].str.strip()
    df['text'] = df['text'].str.lower()
    df['text'] = df['text'].str.strip(',')
    df['text'] = df['text'].str.strip('.')
    df['text'] = df['text'].str.strip('1.')
    df['text'] = df['text'].str.strip(' ')
    df = df[df['label'] == 'DIAGNOSIS']
    df.drop(columns=['Unnamed: 0', 'index', 'label'], inplace=True)
    return df

def identify_laterality(notes):
    patterns = {
    'left eye': r'\bleft\b|\bos\b',
    'right eye': r'\bright\b|\bod\b',
    'both eyes': r'\bbilateral\b|\bbilaterality\b|\bou\b'
    }

    laterality = ''
    for key, pattern in patterns.items():
        if re.search(pattern, notes, re.IGNORECASE):
            laterality = key
    return laterality

def add_laterality_label(df, notes_column='text'):
    laterality_column = []
    for notes in df[notes_column]:
        laterality = identify_laterality(notes.lower())
        if laterality:
            laterality_column.append(laterality)
        else:
            laterality_column.append('not specified')
    df['laterality'] = laterality_column
    return df

def main():
    df = clean_data('task2_full_data.csv')
    add_laterality_label(df)
    df.to_csv('labeled_diagnosis_laterality.csv', index=False)


if __name__ ==  '__main__':
    main()