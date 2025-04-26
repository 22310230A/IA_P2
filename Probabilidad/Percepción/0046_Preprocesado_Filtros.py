# Preprocesado: Filtros
#
# Aplicamos filtros simples para mejorar una imagen:
# desenfoque (suavizado) y detección de bordes básicos.

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
import cv2

# Crear imagen de prueba: cuadrado blanco sobre fondo negro
imagen = np.zeros((100, 100), dtype=np.uint8)
cv2.rectangle(imagen, (25, 25), (75, 75), 255, -1)

# Aplicar un filtro de desenfoque (Blur)
imagen_desenfocada = cv2.GaussianBlur(imagen, (5, 5), 0)

# Aplicar filtro de Sobel para detección de bordes
gradiente_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
gradiente_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)
bordes = cv2.magnitude(gradiente_x, gradiente_y)

# Mostrar resultados
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.title("Imagen Original")
plt.imshow(imagen, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Imagen Desenfocada")
plt.imshow(imagen_desenfocada, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Detección de Bordes")
plt.imshow(bordes, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
