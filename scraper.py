import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://books.toscrape.com/catalogue/page-{}.html'
page = 1

while True:
    url = BASE_URL.format(page)
    response = requests.get(url)

    # Si ya no hay más páginas, salimos del bucle
    if response.status_code != 200:
        print(f"No se encontró la página {page}. Fin del scraping.")
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    # Si no se encontraron libros, salimos
    if not books:
        print(f"No se encontraron libros en la página {page}.")
        break

    print(f"\n📘 Página {page}:")

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()

        print(f'{title} - {price} - {availability}')

    page += 1
