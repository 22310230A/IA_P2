# Árbol de Regresión estilo M5 (simulado)
#
# M5 es un algoritmo que combina árboles de decisión con regresiones lineales
# en las hojas para predecir valores continuos.

from sklearn.tree import DecisionTreeRegressor
import numpy as np

# Datos de entrenamiento (horas estudiadas vs calificación)
X = np.array([[1], [2], [3], [4], [5], [6], [7]]).reshape(-1, 1)
y = np.array([50, 55, 60, 65, 70, 75, 80])

# Crear modelo de árbol de regresión
modelo = DecisionTreeRegressor(max_depth=2)  # controlamos la profundidad
modelo.fit(X, y)

# Nueva predicción
nueva_entrada = np.array([[4.5]])
prediccion = modelo.predict(nueva_entrada)

print("[Árbol de Regresión - Estilo M5]")
print(f"Horas estudiadas: {nueva_entrada[0][0]}")
print(f"Calificación estimada: {prediccion[0]}")
