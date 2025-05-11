import requests
from bs4 import BeautifulSoup

# URL de la pagina a scrapear
URL = 'http://books.toscrape.com/'
response = requests.get(URL)

# Comprobamos
if response.status_code != 200:
    print('Error al acceder a la página:', response.status_code)
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')

for book in books:
    title = book.h3.a['title']

    price = book.find('p', class_='price_color').text

    availability = book.find('p', class_='instock availability').text.strip()
    print(f'{title} - {price} - {availability}')