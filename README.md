# Sprint7
# Sprint7: Análisis de Vehículos Usados

## Descripción del Proyecto
Este proyecto analiza un conjunto de datos de vehículos usados en EE.UU. (`vehicles_us.csv`) para explorar patrones en precios, kilometraje, y otros atributos. La aplicación web, desarrollada con Streamlit, proporciona un cuadro de mandos interactivo para visualizar y filtrar los datos.

## Funcionalidad de la Aplicación Web
La aplicación (`app.py`) permite a los usuarios:
- Ver un resumen del dataset (número de filas y columnas).
- Generar visualizaciones interactivas usando Plotly:
  - **Histograma**: Distribución de precios por tipo de combustible, activado mediante una casilla de verificación.
  - **Gráfico de dispersión**: Precio vs. kilometraje, coloreado por año del modelo, activado mediante una casilla de verificación.
- Explorar el dataset en un Jupyter Notebook (`notebooks/EDA.ipynb`) con análisis exploratorio detallado.

## Estructura del Proyecto
- `app.py`: Aplicación web de Streamlit.
- `notebooks/EDA.ipynb`: Análisis exploratorio con visualizaciones.
- `vehicles_us.csv`: Conjunto de datos.
- `requirements.txt`: Dependencias del proyecto.