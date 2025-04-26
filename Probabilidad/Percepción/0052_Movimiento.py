# Movimiento
#
# Simulamos la detección de movimiento entre dos imágenes
# usando la diferencia de fotogramas.

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
import cv2

# Crear dos imágenes simuladas
imagen1 = np.zeros((100, 100), dtype=np.uint8)
imagen2 = np.zeros((100, 100), dtype=np.uint8)

# Dibujar un cuadrado en diferente posición
cv2.rectangle(imagen1, (30, 30), (50, 50), 255, -1)
cv2.rectangle(imagen2, (40, 40), (60, 60), 255, -1)

# Calcular la diferencia absoluta
diferencia = cv2.absdiff(imagen1, imagen2)

# Umbral para resaltar cambios
_, movimiento = cv2.threshold(diferencia, 30, 255, cv2.THRESH_BINARY)

# Mostrar resultados
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.title("Imagen 1")
plt.imshow(imagen1, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Imagen 2")
plt.imshow(imagen2, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Movimiento Detectado")
plt.imshow(movimiento, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
