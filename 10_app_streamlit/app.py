import streamlit as st
import joblib
import pandas as pd

# 1. Cargar el modelo que guardamos ayer
modelo = joblib.load('mi_modelo_inteligente.pkl')

# 2. Título y descripción de la Web
st.title("🤖 El Predictor del Futuro")
st.write("Introduce tus datos y la IA te dirá el resultado.")

# 3. Crear los inputs (Los controles para el usuario)
# Supongamos que predecimos el precio de una casa basándonos en M2 y Habitaciones
metros = st.number_input("Metros Cuadrados", min_value=10, max_value=500, value=80)
habitaciones = st.slider("Número de Habitaciones", 1, 10, 3)

# 4. El Botón Mágico
if st.button("Calcular Precio"):
    # Creamos el formato de datos que espera el modelo
    datos_nuevos = pd.DataFrame([[metros, habitaciones]], columns=['Metros', 'Habitaciones'])
    
    # Hacemos la predicción
    prediccion = modelo.predict(datos_nuevos)[0]
    
    # Enseñamos el resultado en grande y bonito
    st.success(f"El precio estimado es: {prediccion:.2f} €")
    st.balloons() # ¡Efecto especial de globos!
