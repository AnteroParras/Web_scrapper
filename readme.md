# Web Scraper de libros – Books to Scrape

Este proyecto es un scraper hecho en Python que extrae información de todos los libros disponibles en [Books to Scrape](http://books.toscrape.com), una página pensada para practicar scraping.  
Obtiene el título, precio y disponibilidad de cada libro.

Para gestionar una interfaz gráfica se crea un servicio web.

---

## Funcionamiento de la aplicacion

1. Recorre automáticamente todas las páginas del sitio   
2. Extrae información de cada libro
3. Limpia y organiza los datos antes de guardarlos  
4. Una vez analizado los libros se crea un csv que puedes previsualizar y descargar

---

## Requisitos
Instala las dependencias con:

```bash
pip install -r requirements.txt
```

## Metodo de ejecucion del programa
```bash
streamlit run app.py
```

si estas en window asegurate de estar en el .venv:
```bash
source .venv/bin/activate
streamlit run app.py
```

Se ejecutara una pagina web donde puedes poner la pagina web objetivo. Al terminar creara un csv que podras visualizar y descargar

## Notas importantes
Este sitio está diseñado para practicar scraping. No lo uses en sitios reales sin revisar sus términos de uso.

Puedes extender este proyecto para guardar más campos, o crear una interfaz visual con Streamlit.