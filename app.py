import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

# El encabezado de la pagina
st.header('Dashboard de vehículos usados en EUA')

# Casilla de verificación para crear un histograma
hist_checkbox = st.checkbox('Construir histograma', value=False, label_visibility='visible',
                            help='Muestra la frecuencia de cada tipo de vehículo listado')

if hist_checkbox:  # al hacer clic en la casilla

    # crear un histograma del tipo de vehículo
    fig = px.histogram(car_data, x="type", color="type")

    fig.update_layout(title="Distribución por Tipo de vehículo",
                      xaxis_title="Tipo de vehículo",
                      yaxis_title="Cantidad de vehículos")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Botón para crear gráfico de dispersión
scatter_button = st.button(
    'Construir dispersión', help='Muestra la relación entre el año del modelo y los días listados')

if scatter_button:  # al hacer clic en el botón

    st.markdown(
        "💡 **Tip:** Haz *doble clic* en una categoría de la leyenda para observarla de cerca.")

    # crear gráfico de dispersión
    fig = px.scatter(car_data, x="model_year", y="days_listed",
                     color="type", hover_name='model',
                     hover_data=["price", "transmission", "fuel"],
                     opacity=0.6)

    fig.update_layout(
        title="Duración del listado vs Año del Modelo",
        xaxis_title="Año del modelo",
        yaxis_title="Días listados",
        legend_itemclick="toggle",
        legend_itemdoubleclick="toggleothers"
    )

    # mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)
