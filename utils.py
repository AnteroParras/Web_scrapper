import os

import pandas as pd

def clean_text(text):
    return ' '.join(text.strip().split())

def save_to_csv(data, filename):
    folder = os.path.dirname(filename)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f'Datos guardados en {filename}')
