import streamlit as st
from utils.data_processing import load_and_clean_data
from utils.visualization import plot_fuel_type_count, plot_price_distribution

# Cargar datos
data_url = 'https://raw.githubusercontent.com/anfagudelogo-tpt/datasets/refs/heads/main/car_price_dataset.csv'
df = load_and_clean_data(data_url)

# Título y descripción
st.title("Análisis de Vehículos")
st.write("Esta aplicación analiza un dataset de vehículos.")

# Resumen estadístico
st.subheader("Resumen Estadístico")
st.write(df.describe())

# Visualizaciones
st.subheader("Visualizaciones")
st.pyplot(plot_fuel_type_count(df))
st.pyplot(plot_price_distribution(df))

# Filtro por marca
brand = st.text_input("Ingrese una marca de vehículo")
if st.button("Filtrar"):
    filtered_df = df[df['brand'].str.lower() == brand.lower()]
    st.write(filtered_df.describe())
    if not filtered_df.empty:
        st.pyplot(plot_fuel_type_count(filtered_df))
