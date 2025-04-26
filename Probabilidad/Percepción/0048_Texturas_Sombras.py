# Texturas y Sombras
#
# Simulamos una imagen con texturas y efectos de sombras sencillos
# usando variaciones de intensidad en los píxeles.

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

# Crear una imagen de texturas
imagen = np.zeros((100, 100), dtype=np.uint8)

# Generar textura: líneas diagonales
for i in range(0, 100, 5):
    imagen[i:, i] = 150  # valor intermedio para textura

# Agregar una "sombra" difusa
for i in range(100):
    for j in range(100):
        imagen[i, j] = imagen[i, j] + int(80 * (i / 100))  # oscurece de arriba hacia abajo

# Limitar valores (por si acaso)
imagen = np.clip(imagen, 0, 255)

# Mostrar la imagen
plt.figure(figsize=(5, 5))
plt.imshow(imagen, cmap='gray')
plt.title("Simulación de Texturas y Sombras")
plt.axis('off')
plt.show()
