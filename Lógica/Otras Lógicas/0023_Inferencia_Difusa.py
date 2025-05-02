# Lógica Difusa: Inferencia Difusa
#
# Simulamos un sistema difuso con una regla:
# "SI la temperatura ES calor ENTONCES ventilador ES fuerte"

import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt

# Dominio de entrada (temperatura) y salida (velocidad del ventilador)
temperatura = np.linspace(0, 50, 100)
ventilador = np.linspace(0, 10, 100)

# Función de membresía para entrada: "calor"
def grado_calor(t):
    if t <= 20:
        return 0
    elif 20 < t < 30:
        return (t - 20) / 10
    else:
        return 1

# Función de membresía para salida: "ventilador fuerte"
def ventilador_fuerte(v):
    if v <= 4:
        return 0
    elif 4 < v < 7:
        return (v - 4) / 3
    else:
        return 1

# Entrada del sistema (ejemplo)
temp_observada = 28
grado_activacion = grado_calor(temp_observada)

# Inferencia difusa: recorte del conjunto "fuerte"
resultado_inferido = np.minimum(grado_activacion, [ventilador_fuerte(v) for v in ventilador])

# Visualización
plt.figure(figsize=(8, 4))
plt.plot(ventilador, resultado_inferido, label=f"Inferencia para T={temp_observada}°C")
plt.xlabel("Velocidad del ventilador")
plt.ylabel("Grado de pertenencia")
plt.title("Resultado de la inferencia difusa")
plt.grid(True)
plt.legend()
plt.show()
