*Read this in other languages: [English](README.md), [Español](README.es.md).*

# Artificial Intelligence with Python – Code Repository

This repository accompanies the book **Artificial Intelligence with Python** by **John Selles**. It contains all the practical examples, scripts, and notebooks taken directly from the book's chapters.

## Contents

The repository is organized to follow the logical progression of the book:

- **1_EDA.ipynb** — **Exploratory Data Analysis (EDA)** (pandas, matplotlib, seaborn): Practical examples of histograms, box plots, and correlation heatmaps.
- **2_Regression_Linear.ipynb** — **Linear Regression** with scikit-learn (predicting salaries based on years of experience).
- **3_Classification_Tree.ipynb** — **Classification** using `DecisionTreeClassifier`, including a graphical visualization of the decision tree.
- **4_NN_Keras_MLP.ipynb** — **Your First Neural Network** with TensorFlow/Keras (handwritten digit classification using the MNIST dataset).
- **5_diffusion_simulation.py** — **Educational Demo:** A step-by-step simulation showing how a Diffusion Model removes noise from an image.
- **6_transformers_sentiment.py** — **Transformer (Reader):** Using the Hugging Face pipeline with the BETO model for sentiment analysis in Spanish.
- **7_chatgpt_api_assistant.py** — **Transformer (Writer):** Prompt Engineering and API integration to build a custom ChatGPT assistant (Chef Yoda).
- **8_Hyperparameter_Optimization.ipynb** — **Model Optimization:** Training Random Forest and XGBoost models to reduce overfitting and finding the optimal hyperparameters using cross-validation (`GridSearchCV` and `RandomizedSearchCV`).
- **9_Customer_Segmentation_KMeans_PCA.ipynb** — **Unsupervised Learning:** An end-to-end workflow including feature scaling, optimal *k* selection (Elbow Method and Silhouette Score), K-Means clustering, and two-dimensional visualization with PCA.
- **10_Image_Classification_MNIST.ipynb** — **Deep Learning Case Study:** Advanced TensorFlow/Keras neural network training, visualization of learning curves (overfitting detection), and confusion matrix analysis to better understand AI prediction errors.
- **11_generative_ai.ipynb** — Summary and additional exercises covering the Generative AI concepts explained in the book.
- **📁 12_app_streamlit/** — **Final Project:** Contains `train_model.py` and `app.py` for training a machine learning model and deploying it as a web application using Streamlit.

---

## 🚀 Getting Started

### Jupyter Notebooks (`.ipynb`)

**Recommended:** Open them directly in **Google Colab** (no installation required). Simply replace `github.com` with `colab.research.google.com/github` in the notebook URL.

**Local Environment:** Open them using **Jupyter Notebook**, **JupyterLab**, or **Visual Studio Code**.

### Python Scripts (`.py`)

Run them directly from your terminal or command line:

```bash
python filename.py
```

To launch the web application, navigate to the `12_app_streamlit/` folder and run:

```bash
streamlit run app.py
```

---

## 🛠️ Requirements

If you plan to run the code locally, make sure you have **Python 3.8 or later** installed.

Install all required libraries with:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow transformers openai streamlit joblib
```

> **Note:** Google Colab already includes most of these libraries by default.

---

## 📚 Get the Book

You can purchase the book using the following link:

- 🔗 [English Edition:](https://www.amazon.com/dp/B0HC5BJR45)

---

## ⚖️ License and Attribution

This repository is part of the original companion material for the book.

If you plan to use any of the content for commercial purposes, please contact the author to ensure compliance with the applicable copyright and licensing terms.

---

## 🤝 Contributions

If you'd like to improve the examples (add tests, datasets, or enhance the visualizations), feel free to open a **Pull Request** or submit an **Issue** in this repository.
