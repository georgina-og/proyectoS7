# Dashboard de Vehículos Usados en EE.UU.

Se creó una aplicación web interactiva construida con **Streamlit** y **Plotly** que permite visualizar y explorar datos de vehículos usados en Estados Unidos a partir de un archivo CSV (`vehicles_us.csv`).

## Objetivo de la app

Proporcionar una herramienta sencilla y visual para analizar la información disponible sobre vehículos en venta. 

## Funcionalidades principales

- **Histograma interactivo**:
  - Visualiza la distribución de vehículos por tipo, con colores diferenciados.
  - Permite identificar qué tipos de autos son más comunes en el dataset.

- **Gráfico de dispersión**:
  - Analiza la relación entre el **año del vehículo** (`model_year`) y los **días que estuvo listado** (`days_listed`).
  - Utiliza colores para distinguir diferentes **tipos de vehículo**.
  - Ideal para explorar si los vehículos más nuevos duran más o menos tiempo listados en la plataforma.

## Librerías utilizadas

- Python 3
- Streamlit
- Plotly Express
- Pandas
