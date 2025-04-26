# Reconocimiento de Escritura
#
# Simulamos el reconocimiento básico de escritura a mano
# usando detección de contornos sobre una imagen dibujada artificialmente.

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
import cv2

# Crear una imagen artificial que simule "escritura" (líneas irregulares)
imagen = np.zeros((100, 300), dtype=np.uint8)
cv2.putText(imagen, 'AI', (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255), 5, cv2.LINE_AA)

# Aplicar umbral para mejorar contraste
_, imagen_umbral = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)

# Detectar contornos (trazos de escritura)
contornos, _ = cv2.findContours(imagen_umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos encontrados
imagen_contornos = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)
cv2.drawContours(imagen_contornos, contornos, -1, (0, 255, 0), 2)

# Mostrar resultados
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title("Imagen Simulada de Escritura")
plt.imshow(imagen, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Reconocimiento de Trazos")
plt.imshow(imagen_contornos)
plt.axis('off')

plt.tight_layout()
plt.show()
