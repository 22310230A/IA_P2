# Detección de Aristas y Segmentación
#
# Usamos el detector de Canny para encontrar bordes en una imagen
# y segmentamos regiones basándonos en los bordes.

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
import cv2

# Crear una imagen de prueba (cuadrado dentro de un círculo)
imagen = np.zeros((100, 100), dtype=np.uint8)
cv2.circle(imagen, (50, 50), 30, 255, -1)
cv2.rectangle(imagen, (30, 30), (70, 70), 127, -1)

# Detectar bordes usando Canny
bordes = cv2.Canny(imagen, 50, 150)

# Mostrar resultados
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title("Imagen Original")
plt.imshow(imagen, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Detección de Bordes (Canny)")
plt.imshow(bordes, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
