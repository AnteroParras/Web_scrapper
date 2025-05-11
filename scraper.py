import requests
from bs4 import BeautifulSoup
import time
from utils import clean_text, extract_site_name
from urllib.parse import urljoin


def scrape_books(base_url, st=None):
    """
    Scrapea libros desde la URL base.
    Si se pasa 'st' (Streamlit), muestra progreso en la interfaz.
    """
    page = 1
    all_books = []
    start_time = time.time()

    site_name = extract_site_name(base_url)
    if st:
        st.info(f"Fuente: {site_name}")

    while True:
        current_url = base_url.replace('page-1', f'page-{page}')
        response = requests.get(current_url)

        if response.status_code != 200:
            if st: st.warning(f"Página {page} no encontrada. Fin del scraping.")
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('article', class_='product_pod')

        if not books:
            if st: st.warning(f"No se encontraron libros en la página {page}.")
            break

        for book in books:
            title = clean_text(book.h3.a['title'])
            price = book.find('p', class_='price_color').text.strip()
            availability = clean_text(book.find('p', class_='instock availability').text)

            # Link absoluto del libro (opcional)
            partial_link = book.h3.a['href']
            full_link = urljoin(current_url, partial_link)

            all_books.append({
                'Título': title,
                'Precio': price,
                'Disponibilidad': availability,
                'Enlace': full_link,
                'Página': page,
                'Fuente': site_name
            })

        if st:
            st.write(f"✅ Página {page} completada")
            st.progress(min(page / 50, 1.0))  # Simulación de barra de progreso hasta 50 páginas

        page += 1
        time.sleep(0.5)  # Reduce velocidad para simular carga y evitar bloqueo

    tiempo_total = time.time() - start_time
    return all_books, page - 1, tiempo_total
