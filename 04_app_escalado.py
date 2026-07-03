import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# 1. Configuración de la página web
st.set_page_config(page_title="Simulador de Escalado", layout="centered")
st.title("🏡 Simulador de Escalado de Datos")
st.markdown("Compruebe visualmente cómo cambian los ejes cartesianos al aplicar algoritmos de escalado y observe el peligro de los valores atípicos (Outliers).")

# 2. Panel de Control (Usando 'radio' para evitar controles deslizantes o confusos)
st.sidebar.header("Panel de Control")

escalador = st.sidebar.radio(
    "1. Seleccione el tipo de escalado:",
    ("Sin Escalar (Originales)", "Min-Max Scaler", "Standard Scaler")
)

st.sidebar.markdown("---")

tipo_datos = st.sidebar.radio(
    "2. ¿Incluir un valor atípico?",
    ("Datos Normales", "Añadir Mansión (Outlier Extremo)")
)

# 3. Generar datos base consistentes
np.random.seed(42)
habitaciones = np.random.randint(1, 6, 20)
metros = habitaciones * 25 + np.random.randint(10, 40, 20)
df = pd.DataFrame({"Habitaciones": habitaciones, "Metros": metros})

# 4. Lógica del Outlier
if tipo_datos == "Añadir Mansión (Outlier Extremo)":
    outlier = pd.DataFrame({"Habitaciones": [20], "Metros": [1500]})
    df = pd.concat([df, outlier], ignore_index=True)

# 5. Lógica de Escalado Matemática
if escalador == "Min-Max Scaler":
    scaler = MinMaxScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
elif escalador == "Standard Scaler":
    scaler = StandardScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
else:
    df_scaled = df.copy()

# 6. Dibujar el gráfico interactivo
fig, ax = plt.subplots(figsize=(8, 6))
# Pintamos los puntos normales en azul y el outlier (si existe) en rojo para que destaque
colors = ["#e74c3c" if h > 10 else "#2c3e50" for h in df["Habitaciones"]]
ax.scatter(df_scaled["Habitaciones"], df_scaled["Metros"], c=colors, s=80, alpha=0.8, edgecolor="white")

# 7. Adaptación visual de textos según la selección
if escalador == "Sin Escalar (Originales)":
    ax.set_title("Datos Originales (Escalas muy dispares)", fontsize=14, fontweight="bold")
    ax.set_xlabel("Habitaciones")
    ax.set_ylabel("Metros Cuadrados")
elif escalador == "Min-Max Scaler":
    ax.set_title("Min-Max Scaler (Comprimido entre 0 y 1)", fontsize=14, fontweight="bold")
    ax.set_xlabel("Habitaciones Escaladas")
    ax.set_ylabel("Metros Escalados")
elif escalador == "Standard Scaler":
    ax.set_title("Standard Scaler (Centrado en Media 0, Desviación 1)", fontsize=14, fontweight="bold")
    ax.set_xlabel("Habitaciones Estandarizadas")
    ax.set_ylabel("Metros Estandarizados")
    # Líneas para marcar el centro (0,0)
    ax.axhline(0, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    ax.axvline(0, color='gray', linestyle='--', linewidth=1, alpha=0.5)

ax.grid(True, alpha=0.3)

# Mostrar el gráfico en la web
st.pyplot(fig)

# 8. Texto explicativo automático según la selección del usuario
if tipo_datos == "Añadir Mansión (Outlier Extremo)":
    st.warning("⚠️ **Efecto del valor atípico (Outlier):** Al introducir una observación extrema, los datos normales se comprimen en una esquina del gráfico. Note cómo el outlier distorsiona por completo los rangos de Min-Max y altera la desviación en Standard Scaler. En escenarios reales con ruido severo, se recomienda optar por RobustScaler.")
else:
    st.info("💡 **Nota pedagógica sobre la visualización:** ¿Ha notado que la forma de la nube de puntos apenas varía al cambiar de escalador? Esto ocurre porque ambas técnicas son transformaciones lineales que conservan la geometría de los datos. Para ver el efecto real del preprocesamiento, **observe atentamente las etiquetas numéricas de los ejes X e Y**: verá cómo cambian de las unidades originales a rangos de [0, 1] o a valores centrados en 0.")