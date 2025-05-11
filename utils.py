import os
import pandas as pd

from urllib.parse import urlparse


def clean_text(text):
    return ' '.join(text.strip().split())

def save_to_csv(data, filename):
    folder = os.path.dirname(filename)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f'Datos guardados en {filename}')


def extract_site_name(url):
    """
    Extrae un nombre de sitio limpio a partir de una URL.
    Ejemplo: http://books.toscrape.com → books_toscrape
    """
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname  # ej. books.toscrape.com
    if hostname:
        return hostname.replace('.', '_')
    return "sitio_desconocido"