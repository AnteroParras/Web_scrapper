import streamlit as st
from scraper import scrape_books
from utils import save_to_csv
from datetime import datetime

st.set_page_config(page_title="Web Scraper de Libros", layout="centered")

st.title("📚 Web Scraper de Libros")

# Entrada del usuario
url_input = st.text_input("Introduce la URL base (por ejemplo: http://books.toscrape.com/catalogue/page-1.html)",
                          value="http://books.toscrape.com/catalogue/page-1.html")

start_button = st.button("Comenzar scraping")

if start_button and url_input:
    with st.spinner("Scrapeando páginas..."):

        # Scrapeo con feedback visual
        libros, total_paginas, tiempo_total = scrape_books(url_input, st)

        # Nombre del archivo
        fecha_str = datetime.now().strftime("%Y%m%d_%H%M")
        nombre_archivo = f"{libros[0]['Fuente']}_libros_{fecha_str}.csv".replace(" ", "_")
        output_path = f"output/{nombre_archivo}"

        save_to_csv(libros, output_path)

        st.success(f"Scraping completado en {tiempo_total:.2f} segundos ✅")
        st.download_button("📥 Descargar CSV", data=open(output_path, "rb"), file_name=nombre_archivo, mime="text/csv")

        st.subheader("📊 Vista previa:")
        st.dataframe(libros)
