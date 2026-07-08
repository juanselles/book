import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Configuración de la página web
st.set_page_config(page_title="Simulador de Gradiente", layout="centered")

st.title("⛰️ Simulador de Descenso del Gradiente")
st.markdown("Ajuste la **Tasa de Aprendizaje (Learning Rate)** y observe cómo el algoritmo intenta encontrar el fondo del valle (el error mínimo).")

# 2. Panel lateral para los controles del usuario
st.sidebar.header("Configuración")
opcion_lr = st.sidebar.radio(
    "Seleccione la Tasa de Aprendizaje (Alpha):",
    ("Muy Pequeña (0.05)", "Óptima (0.30)", "Demasiado Grande (1.05)")
)

# 3. Lógica para definir el tamaño del paso según la selección
if "Muy Pequeña" in opcion_lr:
    lr = 0.05
    explicacion = "🔹 **Paso muy pequeño:** El algoritmo da pasos tan cortos que tarda demasiado en llegar al mínimo. Es seguro, pero ineficiente computacionalmente."
elif "Óptima" in opcion_lr:
    lr = 0.30
    explicacion = "✅ **Paso óptimo:** El algoritmo desciende con inercia y llega rápidamente al fondo del valle en unos pocos pasos precisos."
else:
    lr = 1.05
    explicacion = "🚨 **¡DIVERGENCIA! (Paso demasiado grande):** El algoritmo salta al otro lado del valle, subiendo cada vez más alto en cada iteración. El modelo matemático se acaba de romper."

st.info(explicacion)

# 4. Funciones matemáticas del entorno
def funcion_perdida(x):
    return x**2  # Una simple parábola en forma de 'U'

def gradiente(x):
    return 2 * x  # La derivada de x^2

# 5. Motor de simulación del Descenso del Gradiente
x_inicial = -4.0  # El montañero empieza alto en la ladera izquierda
iteraciones = 15

historial_x = [x_inicial]
historial_y = [funcion_perdida(x_inicial)]

x_actual = x_inicial
for i in range(iteraciones):
    # Regla de oro: w_nuevo = w_actual - alpha * gradiente
    x_actual = x_actual - lr * gradiente(x_actual)
    historial_x.append(x_actual)
    historial_y.append(funcion_perdida(x_actual))

# 6. Visualización gráfica con Matplotlib
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar la montaña (La función de pérdida)
x_vals = np.linspace(-6, 6, 100)
y_vals = funcion_perdida(x_vals)
ax.plot(x_vals, y_vals, color='black', linewidth=2, label="Función de Pérdida (Error)")

# Dibujar el recorrido del algoritmo
ax.plot(historial_x, historial_y, color='red', marker='o', linestyle='dashed', 
        linewidth=1.5, markersize=6, label="Pasos del algoritmo")

# Formatear el gráfico para que sea didáctico
ax.set_title(f"Descenso del Gradiente (Alpha = {lr})", fontsize=14)
ax.set_xlabel("Valor del Peso (w)", fontsize=12)
ax.set_ylabel("Error (Coste)", fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()

# Truco visual: Si el algoritmo diverge, fijamos los límites para ver cómo se escapa
if lr > 1:
    ax.set_ylim(-5, 40)
    ax.set_xlim(-6, 6)

st.pyplot(fig)