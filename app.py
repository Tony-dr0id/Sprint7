import pandas as pd
import streamlit as st
import plotly.express as px

# Configurar página de Streamlit
st.set_page_config(page_title="Cuadro de Mandos de Vehículos Usados - Sprint7", layout="wide")

# Encabezado
st.header("Análisis de Vehículos Usados en EE.UU.")

# Cargar dataset
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('vehicles_us.csv')
        df['model_year'] = df['model_year'].astype('Int64')
        df['price'] = df['price'].astype(float)
        df['odometer'] = df['odometer'].astype(float)
        df['cylinders'] = df['cylinders'].astype('Int64')
        df['is_4wd'] = df['is_4wd'].astype('Int64')
        df['date_posted'] = pd.to_datetime(df['date_posted'], errors='coerce')
        return df
    except FileNotFoundError:
        st.error("Error: vehicles_us.csv no encontrado en el directorio del proyecto")
        return None

df = load_data()
if df is None:
    st.stop()

# Resumen básico
st.write(f"**Dataset**: {df.shape[0]} filas, {df.shape[1]} columnas")
st.write("**Columnas**: {', '.join(df.columns.tolist())}")

# Sección de visualizaciones
st.header("Visualizaciones Interactivas")

# Casillas de verificación para gráficos
show_histogram = st.checkbox("Mostrar Histograma de Precios por Combustible")
show_scatter = st.checkbox("Mostrar Gráfico de Dispersión: Precio vs. Kilometraje")

# Alternativa con botones (descomentar para usar en lugar de casillas)
# if st.button("Mostrar Histograma de Precios por Combustible"):
#     show_histogram = True
# else:
#     show_histogram = False
# if st.button("Mostrar Gráfico de Dispersión: Precio vs. Kilometraje"):
#     show_scatter = True
# else:
#     show_scatter = False

# Gráfico 1: Histograma
if show_histogram:
    st.write("**Histograma: Distribución de Precios por Tipo de Combustible**")
    fig1 = px.histogram(
        df,
        x="price",
        color="fuel",
        title="Distribución de Precios por Tipo de Combustible",
        labels={"price": "Precio (USD)", "fuel": "Combustible"},
        nbins=50
    )
    st.plotly_chart(fig1, use_container_width=True)
else:
    st.write("Selecciona la casilla para mostrar el histograma.")

# Gráfico 2: Dispersión
if show_scatter:
    st.write("**Gráfico de Dispersión: Precio vs. Kilometraje por Año**")
    df_plot = df.dropna(subset=['price', 'odometer', 'model_year'])
    if not df_plot.empty:
        fig2 = px.scatter(
            df_plot,
            x="odometer",
            y="price",
            color="model_year",
            title="Precio vs. Kilometraje (Coloreado por Año)",
            labels={"odometer": "Kilometraje (millas)", "price": "Precio (USD)", "model_year": "Año"},
            hover_data=["model", "condition"]
        )
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning("No hay datos suficientes para el gráfico de dispersión.")
else:
    st.write("Selecciona la casilla para mostrar el gráfico de dispersión.")