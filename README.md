# Inteligencia Artificial con Python - Notebooks repository

Este repositorio acompaña el libro **"Inteligencia Artificial con Python"** de Juan Ignacio Sellés Rodenas.
Contiene notebooks de ejemplo extraídos y adaptados a partir del contenido del libro. No se han tocado las imágenes originales del manuscrito.


## Contenido

- `1_EDA.ipynb` — Exploratory Data Analysis (pandas, matplotlib, seaborn): ejemplos de histogramas, boxplots, heatmap.
- `2_Regression_Linear.ipynb` — Regresión lineal con scikit-learn (ejemplo simulado).
- `3_Classification_Tree.ipynb` — Clasificación simple con DecisionTreeClassifier y visualización del árbol.
- `4_NN_Keras_MLP.ipynb` — Red neuronal simple con TensorFlow/Keras (ejemplo educativo).
- `5_Diffusion_Toy_Denoising_AE.ipynb` — Demo educativa: denoising autoencoder que ilustra la idea de "quitar ruido" (relacionado con diffusion models).
- `6_Transformers_Intro.ipynb` — Ejemplo de tokenización / pipeline de transformers (requiere instalar `transformers`).

## Cómo usar

Recomendado: abrir en **Google Colab** o en tu entorno local con Jupyter. Para Colab, sube el notebook o crea un nuevo Colab y usa `File -> Upload notebook`.

Requisitos (sugeridos):
- Python 3.8+
- pandas, numpy, matplotlib, seaborn
- scikit-learn
- tensorflow (para notebooks 4 y 5) — en Colab ya está disponible
- transformers (opcional, para notebook 6)

Instalación rápida (entorno local):
```bash
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow transformers
```

## Licencia y atribución

Repositorio creado a partir del manuscrito original. Para referencia del archivo fuente, ver: fileciteturn4file0.

Si vas a usar el contenido con fines comerciales por favor contacta con el autor para respetar derechos y condiciones.

## Contribuciones

Si quieres mejorar los notebooks (añadir tests, datos, o mejorar visualizaciones), abre un *pull request* o un *issue* en el repositorio.

---

_Hecho automáticamente y adaptado para uso educativo._
