# Función de utilidad:
# Representa las preferencias de un agente entre diferentes opciones bajo incertidumbre.
#
# Ejemplo: un robot debe decidir entre 3 rutas con diferentes probabilidades y recompensas esperadas.

opciones = {
    'Ruta A': {'probabilidad': 0.6, 'recompensa': 80},
    'Ruta B': {'probabilidad': 0.3, 'recompensa': 120},
    'Ruta C': {'probabilidad': 0.1, 'recompensa': 200}
}

def utilidad_esperada(prob, recompensa):
    return prob * recompensa

# Calcular y mostrar la utilidad esperada para cada opción
for ruta, valores in opciones.items():
    utilidad = utilidad_esperada(valores['probabilidad'], valores['recompensa'])
    print(f"{ruta}: Utilidad esperada = {utilidad:.2f}")
