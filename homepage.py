import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Olist App",
    page_icon=":earth_americas:",
    layout="wide"
)

#Cargar los datos de la matriz de co-ocurrencia en un DataFrame
matrix_data = pd.read_csv("co-occurrence_matrix.csv")

#Crear una lista de productos para el selectbox
product_list = matrix_data["product_id"].unique()
st.title("Co-occurrence matrix")
selected_product = st.selectbox("Select a product", product_list)
st.write("Selected product:: " + selected_product)

#Filtrar los datos de la matriz para mostrar solo los productos relacionados
filtered_matrix = matrix_data[matrix_data["product_id"] == selected_product]
limit = st.slider("Limit:",0.0,1.0,0.2)
#Filtro solo las columnas numericas y las que superen el slider
filtered_matrix = filtered_matrix[filtered_matrix.select_dtypes(include=[np.number]).columns]
filtered_matrix = filtered_matrix.loc[:, filtered_matrix.apply(lambda x: x.max() > limit)]
#Filtro el producto seleccionado
filtered_matrix = filtered_matrix.drop(selected_product, axis=1)

#Mostrar la matriz de co-ocurrencia en una tabla
st.dataframe(filtered_matrix)
st.markdown("---")