# Mapas Autoorganizados de Kohonen (Self-Organizing Maps - SOM)
#
# Los SOM son redes neuronales no supervisadas que proyectan datos de alta dimensión
# en una representación de menor dimensión preservando la topología.

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
from minisom import MiniSom

# Generamos datos artificiales: dos grupos
np.random.seed(42)
grupo1 = np.random.randn(100, 2) + np.array([2, 2])
grupo2 = np.random.randn(100, 2) + np.array([-2, -2])
datos = np.vstack((grupo1, grupo2))

# Crear y entrenar un SOM
som = MiniSom(x=7, y=7, input_len=2, sigma=1.0, learning_rate=0.5, random_seed=42)
som.random_weights_init(datos)
som.train_random(datos, num_iteration=100)

# Visualizar
plt.figure(figsize=(8, 8))
for i, x in enumerate(datos):
    w = som.winner(x)  # posición del "ganador"
    plt.text(w[0] + 0.5, w[1] + 0.5, str(i),
             color='red' if i < 100 else 'blue', fontdict={'weight': 'bold', 'size': 9})

plt.title("Mapa Autoorganizado de Kohonen (SOM)")
plt.xlim([0, 7])
plt.ylim([0, 7])
plt.grid(True)
plt.show()
