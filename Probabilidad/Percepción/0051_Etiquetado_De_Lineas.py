# Etiquetado de Líneas
#
# Simulamos el etiquetado de diferentes regiones conectadas (líneas o áreas)
# en una imagen, asignándoles un número o color único.

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
import cv2

# Crear una imagen con varias líneas blancas sobre fondo negro
imagen = np.zeros((100, 300), dtype=np.uint8)
cv2.line(imagen, (20, 20), (280, 20), 255, 2)
cv2.line(imagen, (20, 50), (280, 50), 255, 2)
cv2.line(imagen, (20, 80), (280, 80), 255, 2)

# Etiquetar las regiones conectadas
num_labels, etiquetas = cv2.connectedComponents(imagen)

# Asignar colores diferentes a cada línea
etiquetas_color = np.uint8(255 * etiquetas / num_labels)

# Mostrar resultados
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title("Imagen Original")
plt.imshow(imagen, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title(f"Líneas Etiquetadas ({num_labels-1} líneas detectadas)")
plt.imshow(etiquetas_color, cmap='nipy_spectral')
plt.axis('off')

plt.tight_layout()
plt.show()
