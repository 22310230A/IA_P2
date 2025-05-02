# Lógica Difusa: Resumen General
#
# Integra conjuntos difusos, inferencia difusa y lógica tipo Fuzzy CLIPS
# en un solo archivo para evaluar temperatura y decidir la acción del ventilador.

import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt

# Dominio
temperatura = np.linspace(0, 50, 100)
ventilador = np.linspace(0, 10, 100)

# ------------------------
# Conjunto Difuso: "calor"
# ------------------------
def grado_calor(t):
    if t <= 20:
        return 0
    elif 20 < t < 30:
        return (t - 20) / 10
    else:
        return 1

# ------------------------
# Inferencia Difusa
# ------------------------
def ventilador_fuerte(v):
    if v <= 4:
        return 0
    elif 4 < v < 7:
        return (v - 4) / 3
    else:
        return 1

def inferencia_difusa(temp_entrada):
    activacion = grado_calor(temp_entrada)
    salida = np.minimum(activacion, [ventilador_fuerte(v) for v in ventilador])
    return salida

# ------------------------
# Lógica tipo Fuzzy CLIPS
# ------------------------
def clasificar_temp(temp):
    if temp <= 20:
        return 'frio', 1
    elif 20 < temp < 30:
        return 'templado', (30 - temp) / 10
    else:
        return 'calor', 1

def regla_fuzzy_clips(temp):
    estado, grado = clasificar_temp(temp)
    if estado == 'frio':
        accion = 'ventilador apagado'
    elif estado == 'templado':
        accion = 'ventilador medio'
    else:
        accion = 'ventilador fuerte'
    return estado, grado, accion

# ------------------------
# Evaluación completa
# ------------------------
temp_actual = 28
estado, grado, accion = regla_fuzzy_clips(temp_actual)
salida_difusa = inferencia_difusa(temp_actual)

# Mostrar resultados
print("[Resumen General - Lógica Difusa]")
print(f"Temperatura observada: {temp_actual}°C")
print(f"Estado lingüístico: {estado} (grado: {grado:.2f})")
print(f"Acción recomendada: {accion}")

# Visualizar inferencia
plt.figure(figsize=(8, 4))
plt.plot(ventilador, salida_difusa, label=f"Inferencia difusa para T={temp_actual}°C")
plt.xlabel("Velocidad del ventilador")
plt.ylabel("Grado de pertenencia")
plt.title("Resultado de inferencia difusa")
plt.grid(True)
plt.legend()
plt.show()
