import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# 1. Configuración de la página web
st.set_page_config(page_title="Simulador de Gradiente", layout="centered")

st.title("⛰️ Simulador de Descenso del Gradiente")
st.markdown("Ajuste la **Tasa de Aprendizaje (Learning Rate)** y pulse el botón de **Play** para ver la animación fotograma a fotograma.")

# 2. Panel lateral para los controles del usuario
st.sidebar.header("Configuración")
opcion_lr = st.sidebar.radio(
    "Seleccione la Tasa de Aprendizaje (Alpha):",
    ("Muy Pequeña (0.05)", "Óptima (0.30)", "Demasiado Grande (1.05)")
)

if "Muy Pequeña" in opcion_lr:
    lr = 0.05
elif "Óptima" in opcion_lr:
    lr = 0.30
else:
    lr = 1.05

def funcion_perdida(x):
    return x**2

def gradiente(x):
    return 2 * x

# 3. Espacio reservado para el gráfico animado
grafico_placeholder = st.empty()
mensaje_placeholder = st.empty()

# 4. Botón PLAY y motor de la animación
if st.button("▶️ Iniciar Simulación (Play)"):
    x_actual = -4.0
    historial_x = [x_actual]
    historial_y = [funcion_perdida(x_actual)]

    # Animamos 15 pasos (iteraciones)
    for i in range(15):
        # Matemática del descenso
        x_actual = x_actual - lr * gradiente(x_actual)
        historial_x.append(x_actual)
        historial_y.append(funcion_perdida(x_actual))

        # Dibujar el fotograma
        fig, ax = plt.subplots(figsize=(8, 5))
        x_vals = np.linspace(-6, 6, 100)
        ax.plot(x_vals, funcion_perdida(x_vals), color='black', linewidth=2, label="Función de Pérdida")
        ax.plot(historial_x, historial_y, color='red', marker='o', linestyle='dashed', linewidth=1.5, markersize=6, label="Pasos del algoritmo")
        
        ax.set_title(f"Iteración {i+1} | Alpha = {lr}", fontsize=14)
        ax.set_xlabel("Valor del Peso (w)", fontsize=12)
        ax.set_ylabel("Error (Coste)", fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend(loc="upper center")

        # Ajuste visual para que la divergencia no rompa la pantalla
        if lr > 1:
            ax.set_ylim(-5, 40)
            ax.set_xlim(-6, 6)
        else:
            ax.set_ylim(-2, 20)
            ax.set_xlim(-6, 6)

        # Mostrar fotograma y pausar
        grafico_placeholder.pyplot(fig)
        plt.close(fig) # Evita sobrecarga de memoria
        time.sleep(0.4) # Velocidad de la animación (0.4 segundos por paso)
        
    # Mensaje final al terminar la animación
    if lr == 0.05:
        mensaje_placeholder.info("🔹 **Conclusión:** El algoritmo da pasos tan cortos que es seguro, pero no logra llegar al fondo en 15 iteraciones. Tarda demasiado.")
    elif lr == 0.30:
        mensaje_placeholder.success("✅ **Conclusión:** ¡Perfecto! El algoritmo llega al fondo del valle en muy pocos pasos y se estabiliza.")
    else:
        mensaje_placeholder.error("🚨 **Conclusión:** ¡DIVERGENCIA! El paso es tan grande que salta al otro lado del valle, subiendo cada vez más. El modelo matemático ha colapsado.")

else:
    # Estado inicial estático (antes de pulsar Play)
    fig, ax = plt.subplots(figsize=(8, 5))
    x_vals = np.linspace(-6, 6, 100)
    ax.plot(x_vals, funcion_perdida(x_vals), color='black', linewidth=2, label="Función de Pérdida")
    ax.plot([-4.0], [16.0], color='red', marker='o', markersize=8, label="Posición de Salida")
    ax.set_title(f"Preparado (Alpha = {lr}) - Pulse Play para comenzar", fontsize=14)
    ax.set_xlabel("Valor del Peso (w)", fontsize=12)
    ax.set_ylabel("Error (Coste)", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.6)
    if lr > 1:
        ax.set_ylim(-5, 40)
    else:
        ax.set_ylim(-2, 20)
    grafico_placeholder.pyplot(fig)