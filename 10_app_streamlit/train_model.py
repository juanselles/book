import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# 1. Inventamos un "histórico" de datos de casas para que la IA aprenda
datos_casas = {
    'Metros': [50, 80, 120, 200, 60, 90, 150, 250],
    'Habitaciones': [1, 2, 3, 4, 2, 3, 4, 5],
    'Precio': [100000, 160000, 250000, 420000, 120000, 180000, 310000, 500000]
}

df = pd.DataFrame(datos_casas)

# X son las preguntas, y es la respuesta
X = df[['Metros', 'Habitaciones']]
y = df['Precio']

# 2. Creamos y entrenamos el cerebro (Random Forest suele ser muy bueno)
modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X, y)

# 3. ¡Magia! Guardamos la partida
joblib.dump(modelo, 'mi_modelo_inteligente.pkl')

print("¡Éxito! El archivo 'mi_modelo_inteligente.pkl' acaba de aparecer en tu carpeta.")
