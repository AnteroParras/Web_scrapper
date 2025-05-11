# Web Scraper de libros – Books to Scrape

Este proyecto es un scraper hecho en Python que extrae información de todos los libros disponibles en [Books to Scrape](http://books.toscrape.com), una página pensada para practicar scraping.  
Obtiene el título, precio y disponibilidad de cada libro, y guarda los datos en un archivo CSV ( en una carpeta output ).

---

## Funcionamiento del script

1. Recorre automáticamente todas las páginas del sitio   
2. Extrae información de cada libro
3. Guarda los resultados en `output/libros.csv`  
4. Crea la carpeta `output/` si no existe
5. Limpia y organiza los datos antes de guardarlos  

---

## Requisitos

- Python 3.8+
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [pandas](https://pypi.org/project/pandas/)

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

## Metodo de ejecucion del programa
```bash
python scraper.py
```
Se generará un archivo ``libros.csv`` en la carpeta ``output/`` con todos los datos extraídos.

## Notas importantes
Este sitio está diseñado para practicar scraping. No lo uses en sitios reales sin revisar sus términos de uso.

Puedes extender este proyecto para guardar más campos, o crear una interfaz visual con Streamlit.