import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Metodologías para el Proceso de minería de Datos")
st.write("PRACTICA 1")

#Dataframe de Productos
data = {
    "Producto": ['Laptop', "Smartphone", 'Tablet', 'Monitor', 'Teclado'],
    "Precio": [1000, 500, 300, 200, 50],
    "Stock": [10, 20, 15, 5, 30]
}
df = pd.DataFrame(data)
st.subheader("DataFrame de Productos")
st.dataframe(df)
st.write("Graficas")
st.header("Gráfica de Precios de Productos")
fig, ax = plt.subplots()
ax.bar(df['Producto'], df['Precio'], color='blue')
ax.set_xlabel('Producto')
ax.set_ylabel('Precio')
ax.set_title('Precios de Productos')
st.pyplot(fig)

st.header("Gráfica de Cantidad de Productos")
fig, ax = plt.subplots()
ax.bar(df['Producto'], df['Stock'], color='orange')
ax.set_xlabel('Producto')
ax.set_ylabel('Stock')
ax.set_title('Cantidad de Productos')
st.pyplot(fig)