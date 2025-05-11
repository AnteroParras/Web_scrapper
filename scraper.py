import requests
from bs4 import BeautifulSoup
import time
from utils import clean_text, save_to_csv

BASE_URL = 'http://books.toscrape.com/catalogue/page-{}.html'
page = 1
all_books = []

while True:
    url = BASE_URL.format(page)
    response = requests.get(url)

    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    if not books:
        break

    for book in books:
        title = clean_text(book.h3.a['title'])
        price = book.find('p', class_='price_color').text.strip()
        availability = clean_text(book.find('p', class_='instock availability').text)

        all_books.append({
            'Título': title,
            'Precio': price,
            'Disponibilidad': availability
        })

    page += 1
    time.sleep(1)

# Guardamos en CSV
save_to_csv(all_books, 'output/libros.csv')
