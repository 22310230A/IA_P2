# Boosting con AdaBoost (ejemplo básico)
#
# Boosting combina varios modelos débiles para crear uno fuerte.
# En este caso usamos AdaBoost para clasificar si un estudiante pasará o no.

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Datos de ejemplo: [horas de estudio, cantidad de tareas entregadas]
X = np.array([
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 2],
    [5, 3],
    [6, 4],
    [7, 4]
])

# Etiquetas: 0 = no pasa, 1 = pasa
y = np.array([0, 0, 0, 1, 1, 1, 1])

# Crear modelo base débil (árbol simple)
base_modelo = DecisionTreeClassifier(max_depth=1)

# Crear el modelo Boosting
modelo = AdaBoostClassifier(estimator=base_modelo, n_estimators=10)

modelo.fit(X, y)

# Predicción
entrada = np.array([[4, 2]])  # estudiante con 4h de estudio y 2 tareas
resultado = modelo.predict(entrada)

print("[Boosting con AdaBoost]")
print("Entrada:", entrada[0])
print("¿Pasa el curso?:", "Sí" if resultado[0] == 1 else "No")
