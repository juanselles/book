*Leer en otros idiomas: [English](README.en.md), [Español](README.md).*


# Inteligencia Artificial con Python - Repositorio de Código

Este repositorio acompaña al libro **"Inteligencia Artificial con Python"** de Juan Ignacio Sellés. Contiene todos los ejemplos prácticos, scripts y notebooks extraídos directamente de los capítulos.


## Contenido

El repositorio está estructurado para seguir la progresión lógica del libro:
*   **`1_EDA.ipynb`** — Análisis Exploratorio de Datos (*pandas, matplotlib, seaborn*): Ejemplos prácticos de histogramas, boxplots y mapas de calor de correlación.
*   **`2_Regression_Linear.ipynb`** — Regresión Lineal con *scikit-learn* (predicción de salarios basada en la experiencia).
*   **`3_Classification_Tree.ipynb`** — Clasificación Simple con *DecisionTreeClassifier* y visualización gráfica del árbol.
*   **`4_NN_Keras_MLP.ipynb`** — Primera Red Neuronal con *TensorFlow/Keras* (clasificación de dígitos escritos a mano con MNIST).
*   **`5_diffusion_simulation.py`** — Demo educativa: Una simulación paso a paso de cómo un Modelo de Difusión elimina el ruido de una imagen.
*   **`6_transformers_sentiment.py`** — Transformer (Lector): Uso del `pipeline` de Hugging Face con el modelo BETO para análisis de sentimientos en español.
*   **`7_chatgpt_api_assistant.py`** — Transformer (Escritor): Ingeniería de Prompts (Prompt Engineering) y conexión a la API para crear un asistente ChatGPT personalizado (Chef Yoda).
*   **`8_Hyperparameter_Optimization.ipynb`** — Optimización de Modelos: Entrenamiento de Random Forest y XGBoost para evitar el sobreajuste (overfitting), y búsqueda de las configuraciones óptimas usando validación cruzada (GridSearchCV y RandomizedSearchCV).
*   **`9_Customer_Segmentation_KMeans_PCA.ipynb`** — Aprendizaje No Supervisado: Flujo de trabajo analítico aplicando escalado, búsqueda del k óptimo (Codo y Silhouette), agrupamiento con K-Means y reducción de dimensionalidad bidimensional con PCA.
*   **`10_Image_Classification_MNIST.ipynb`** — Análisis forense con Deep Learning: Entrenamiento avanzado de una red neuronal con TensorFlow/Keras, visualización de las curvas de aprendizaje (overfitting) y matriz de confusión para entender los errores visuales de la IA.
*   **`11_generative_ai.ipynb`** — Resumen y ejercicios extra relacionados con los conceptos de IA Generativa explicados en el libro.
*   **📁 `12_app_streamlit/`** — Carpeta del Proyecto Final: Contiene `train_model.py` y `app.py` para entrenar un modelo y desplegarlo como una aplicación web usando Streamlit.

## 🚀 Cómo usarlo

**Para los Jupyter Notebooks (archivos `.ipynb`):**
*   **Recomendado:** Ábrelos directamente en **Google Colab** (no requiere instalación). Simplemente puedes reemplazar `github.com` con `colab.research.google.com/github` en la URL de cualquier archivo notebook.
*   **Entorno Local:** Ábrelos usando Jupyter Notebook, JupyterLab o VS Code.

**Para los Scripts de Python (archivos `.py`):**
*   Ejecútalos directamente en tu terminal o línea de comandos: `python nombre_del_archivo.py`
*   Para ejecutar la aplicación web, navega hasta la carpeta `app_streamlit/` y escribe: `streamlit run app.py`

## 🛠️ Requisitos

Si vas a ejecutar el código localmente, asegúrate de tener instalado Python 3.8 o superior. Puedes instalar todas las librerías necesarias con un solo comando:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow transformers openai streamlit joblib
```
(Nota: Google Colab ya tiene la mayoría de estas librerías preinstaladas)..

## 📚 Encuentra el libro
Puedes adquirir el libro en usando los siguiente enlace:

🔗 [Versión en Español](https://www.amazon.es/dp/B0GDMKVZBK)

## ⚖️ Licencia y Atribución

Este repositorio es parte del contenido original del libro. Para referencia, visita: https://www.amazon.es/dp/B0GDMKVZBK.

Si planeas usar el contenido con fines comerciales, por favor contacta al autor para respetar los derechos y condiciones.

## 🤝 Contribuciones

Si te gustaría mejorar los ejemplos (añadir pruebas, datos o mejorar las visualizaciones), siéntete libre de abrir un pull request o un issue en el repositorio.
