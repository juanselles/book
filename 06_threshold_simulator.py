import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

# Configuración inicial de la página web
st.set_page_config(page_title="Simulador de Umbral de Decisión", layout="centered")

st.title("🔬 Simulador de Umbral de Decisión (Threshold)")
st.markdown("""
Esta herramienta interactiva muestra cómo cambia la **Matriz de Confusión** y las métricas de evaluación 
cuando movemos el límite matemático (*threshold*) para diagnosticar a 100 pacientes simulados.
""")

# 1. GENERACIÓN DE DATOS SIMULADOS (Fijos y reproducibles)
@st.cache_data
def generar_datos():
    np.random.seed(42)
    # 50 pacientes sanos (Clase 0) y 50 pacientes enfermos (Clase 1)
    y_real = np.array([0] * 50 + [1] * 50)
    
    # El modelo asigna probabilidades bajas a los sanos y altas a los enfermos, con cierto solape
    prob_sanos = np.random.beta(2, 5, 50)      # Concentradas cerca de 0.2
    prob_enfermos = np.random.beta(5, 2, 50)   # Concentradas cerca de 0.8
    y_probabilidades = np.concatenate([prob_sanos, prob_enfermos])
    
    return y_real, y_probabilidades

y_real, y_probabilidades = generar_datos()

# 2. INTERFAZ DE USUARIO (Panel de Control)
st.subheader("Ajuste del Umbral Matemático")
umbral = st.slider(
    "Seleccione el umbral de decisión (Threshold):",
    min_value=0.05,
    max_value=0.95,
    value=0.50,
    step=0.05
)

st.markdown(f"**Criterio actual:** Si la probabilidad calculada es $\ge$ **{umbral:.2f}**, el paciente se diagnostica como **ENFERMO**.")

# 3. CÁLCULO DE PREDICCIONES SEGÚN EL UMBRAL ELEGIDO
y_pred = (y_probabilidades >= umbral).astype(int)

# Calcular componentes de la matriz de confusión
tn, fp, fn, tp = confusion_matrix(y_real, y_pred).ravel()

# Calcular métricas globales
precision = precision_score(y_real, y_pred, zero_division=0)
recall = recall_score(y_real, y_pred, zero_division=0)
f1 = f1_score(y_real, y_pred, zero_division=0)

# 4. VISUALIZACIÓN GRÁFICA (Matriz de Confusión)
st.subheader("Matriz de Confusión Resultante")

fig, ax = plt.subplots(figsize=(5, 3.5))
matriz_datos = [[tn, fp], [fn, tp]]
etiquetas = [
    [f"Verdadero Negativo\n(Sanos Detectados)\nTN = {tn}", f"Falso Positivo\n(Alarma Falsa)\nFP = {fp}"],
    [f"Falso Negativo\n(Enfermos Omitidos)\nFN = {fn}", f"Verdadero Positivo\n(Enfermos Detectados)\nTP = {tp}"]
]

sns.heatmap(
    matriz_datos, 
    annot=etiquetas, 
    fmt="", 
    cmap="Blues", 
    cbar=False,
    xticklabels=["Predicho: SANO", "Predicho: ENFERMO"],
    yticklabels=["Real: SANO", "Real: ENFERMO"],
    ax=ax
)
plt.ylabel("Realidad")
plt.xlabel("Predicción del Modelo")
plt.tight_layout()
st.pyplot(fig)

# 5. PANEL DE MÉTRICAS COMPLEMENTARIAS
st.subheader("Métricas de Rendimiento")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Precisión (Precision)", value=f"{precision*100:.1f} %")
    st.caption("¿Cuántos de los diagnosticados como enfermos lo están de verdad?")

with col2:
    st.metric(label="Exhaustividad (Recall)", value=f"{recall*100:.1f} %")
    st.caption("¿Qué porcentaje de enfermos reales ha logrado cazar el modelo?")

with col3:
    st.metric(label="Puntuación F1 (F1 Score)", value=f"{f1*100:.1f} %")
    st.caption("Equilibrio armónico entre la Precisión y el Recall.")

# 6. EXPLICACIÓN DIDÁCTICA DINÁMICA
st.subheader("💡 Lección práctica para el lector")
if umbral < 0.40:
    st.info(
        f"**Umbral Bajo ({umbral:.2f}):** El modelo es muy sensible. Al mínimo síntoma diagnostica como enfermo. "
        f"Resultado: El **Recall** es excelente ({recall*100:.0f}%), casi no se escapa ningún enfermo (FN = {fn}). "
        f"Sin embargo, la **Precisión** cae porque hay muchas alarmas falsas (FP = {fp}). "
        "Ideal si omitir un caso cuesta vidas."
    )
elif umbral > 0.60:
    st.warning(
        f"**Umbral Alto ({umbral:.2f}):** El modelo es muy conservador. Solo diagnostica enfermedad si está segurísimo. "
        f"Resultado: La **Precisión** sube ({precision*100:.0f}%), las alertas son muy fiables (FP = {fp}). "
        f"A cambio, la **Exhaustividad (Recall)** se desploma porque muchos enfermos reales se van a casa sin detectar (FN = {fn}). "
        "Ideal si el tratamiento médico es muy peligroso o invasivo."
    )
else:
    st.success(
        f"**Umbral Equilibrado ({umbral:.2f}):** Se busca un punto medio estándar. "
        f"La combinación de aciertos ofrece un F1-Score del {f1*100:.0f}%. Observe cómo al mover el control "
        "hacia los lados una métrica mejora a costa de perjudicar a la otra."
    )