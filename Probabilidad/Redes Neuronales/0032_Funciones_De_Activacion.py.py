# Funciones de Activación
#
# Las funciones de activación deciden si una neurona artificial se "activa" o no.
# Ayudan a introducir no linealidad en la red neuronal, permitiendo modelar problemas complejos.

import numpy as np
import matplotlib
matplotlib.use('TkAgg')  
import matplotlib.pyplot as plt

# Definimos algunas funciones de activación comunes
def escalon(x):
    return np.where(x >= 0, 1, 0)

def sigmoide(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

# Rango de valores
x = np.linspace(-5, 5, 200)

# Calcular las salidas
y_escalon = escalon(x)
y_sigmoide = sigmoide(x)
y_tanh = tanh(x)
y_relu = relu(x)

# Graficar
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(x, y_escalon)
plt.title("Función Escalón")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(x, y_sigmoide)
plt.title("Función Sigmoide")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(x, y_tanh)
plt.title("Función Tanh")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(x, y_relu)
plt.title("Función ReLU")
plt.grid(True)

plt.tight_layout()
plt.show()
