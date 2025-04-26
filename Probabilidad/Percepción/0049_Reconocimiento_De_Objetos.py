# Reconocimiento de Objetos
#
# Simulamos el reconocimiento básico de objetos usando detección de contornos
# en una imagen sencilla.

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
import cv2

# Crear imagen de prueba: dos círculos
imagen = np.zeros((200, 200), dtype=np.uint8)
cv2.circle(imagen, (60, 60), 30, 255, -1)
cv2.circle(imagen, (140, 140), 40, 255, -1)

# Detectar contornos
contornos, _ = cv2.findContours(imagen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar contornos detectados
imagen_contornos = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)
cv2.drawContours(imagen_contornos, contornos, -1, (0, 255, 0), 2)

# Mostrar resultados
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.title("Imagen Original")
plt.imshow(imagen, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Reconocimiento de Objetos")
plt.imshow(imagen_contornos)
plt.axis('off')

plt.tight_layout()
plt.show()
