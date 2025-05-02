# Lógica Difusa: Conjuntos Difusos
#
# Simulamos un conjunto difuso que representa la pertenencia parcial
# de temperaturas a la categoría "calor".

import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt

# Dominio: temperaturas de 0°C a 50°C
temperaturas = np.linspace(0, 50, 100)

# Función de membresía: "calor"
def calor(t):
    if t <= 20:
        return 0
    elif 20 < t < 30:
        return (t - 20) / 10
    else:
        return 1

# Aplicamos la función de membresía a todo el dominio
membresias = np.array([calor(t) for t in temperaturas])

# Mostrar resultados
plt.figure(figsize=(8, 4))
plt.plot(temperaturas, membresias, label="Conjunto difuso: 'calor'")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Grado de pertenencia")
plt.title("Función de membresía difusa para 'calor'")
plt.grid(True)
plt.legend()
plt.show()
