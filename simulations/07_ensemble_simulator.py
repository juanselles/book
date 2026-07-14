import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.ensemble import RandomForestClassifier

# Configuración de la página
st.set_page_config(page_title="Simulador de Random Forest", layout="centered")

st.title("🌲 Simulador: Random Forest vs Overfitting")
st.markdown("""
Descubra cómo la **profundidad del árbol** provoca memorización (*Overfitting*) y cómo 
añadir **más árboles** (*Random Forest*) suaviza las decisiones y estabiliza el modelo.
""")

# 1. GENERACIÓN DE DATOS (Patrón de medias lunas con ruido)
@st.cache_data
def generar_datos():
    X, y = make_moons(n_samples=300, noise=0.3, random_state=42)
    return X, y

X, y = generar_datos()

# 2. CONTROLES DE USUARIO
col1, col2 = st.columns(2)
with col1:
    max_depth = st.slider("Profundidad del Árbol (max_depth):", min_value=1, max_value=20, value=2)
    st.caption("A mayor profundidad, más se ajusta el modelo a los datos concretos.")
with col2:
    n_estimators = st.slider("Número de Árboles (n_estimators):", min_value=1, max_value=100, value=1)
    st.caption("Si es 1, es un Árbol simple. Si es >1, es un Bosque Aleatorio.")

# 3. ENTRENAMIENTO DEL MODELO EN TIEMPO REAL
modelo = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
modelo.fit(X, y)

# 4. VISUALIZACIÓN DE LA FRONTERA DE DECISIÓN
st.subheader("Mapa de Decisión del Algoritmo")

fig, ax = plt.subplots(figsize=(8, 5))

# Crear una cuadrícula de puntos para pintar el fondo
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

# Predecir el color de cada punto del fondo
Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Dibujar el fondo y los puntos
ax.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
ax.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap='coolwarm', s=40)

ax.set_title(f"Modelo: {n_estimators} árbol(es) | Profundidad: {max_depth}")
ax.set_xlabel("Característica 1")
ax.set_ylabel("Característica 2")
st.pyplot(fig)

# 5. DIAGNÓSTICO DIDÁCTICO
st.markdown("---")
if n_estimators == 1 and max_depth > 10:
    st.error("**⚠️ ALERTA DE OVERFITTING (Alta Varianza):** Tiene un solo árbol muy profundo. Fíjese cómo el fondo ha creado 'islas' diminutas de color solo para capturar puntos aislados (ruido). El modelo ha memorizado los datos de entrenamiento y fallará en el mundo real.")
elif n_estimators > 20 and max_depth > 10:
    st.success("**✅ LA MAGIA DEL BOSQUE:** Aunque la profundidad es alta, al usar muchos árboles las decisiones se promedian. Las fronteras son mucho más suaves y naturales. ¡El Random Forest ha curado el Overfitting!")
elif max_depth < 3:
    st.warning("**⚠️ ALERTA DE UNDERFITTING (Alto Sesgo):** El modelo es demasiado simple. La línea de separación es demasiado recta o cuadriculada y no logra capturar la curva real de los datos. Necesita más profundidad.")
else:
    st.info("**⚖️ EQUILIBRIO:** El modelo está empezando a capturar la tendencia general sin volverse excesivamente caótico. ¡Buen trabajo ajustando los parámetros!")