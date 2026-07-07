import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Anuncios de venta de coches — Dashboard')

# histograma con checkbox
build_histogram = st.checkbox('Construir histograma del odómetro')
if build_histogram:
    st.write('Distribución del odómetro de los vehículos')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)


# Scatter

build_scatter = st.checkbox('Construir gráfico de dispersión odómetro vs precio')
if build_scatter:
    st.write('Relación entre el kilometraje y el precio de los vehículos')
    fig = px.scatter(car_data, x='odometer',  y='price')
    st.plotly_chart(fig, use_container_width=True)