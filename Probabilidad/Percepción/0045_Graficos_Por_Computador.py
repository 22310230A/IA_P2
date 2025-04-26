# Gráficos por Computador
#
# Simulamos la creación de una imagen simple usando programación
# para ilustrar los conceptos básicos de gráficos por computador.

import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt

# Creamos una imagen de 100x100 píxeles
imagen = np.zeros((100, 100, 3), dtype=np.uint8)  # 3 canales RGB

# Dibujar un cuadrado rojo
imagen[20:80, 20:80] = [255, 0, 0]  # Rojo en el centro

# Dibujar una línea azul
for i in range(100):
    imagen[i, i] = [0, 0, 255]

# Mostrar la imagen
plt.figure(figsize=(5, 5))
plt.imshow(imagen)
plt.title("Gráficos por Computador - Imagen Básica")
plt.axis('off')
plt.show()
