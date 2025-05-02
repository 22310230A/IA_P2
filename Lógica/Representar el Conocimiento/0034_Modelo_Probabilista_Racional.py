# Modelo Probabilista Racional
#
# Simulamos una decisión racional basada en utilidad esperada:
# elegir entre opciones según su probabilidad y ganancia.

# Opciones disponibles
opciones = {
    'viajar_en_auto': {'probabilidad': 0.7, 'utilidad': 8},
    'viajar_en_camion': {'probabilidad': 0.9, 'utilidad': 5},
    'no_viajar': {'probabilidad': 1.0, 'utilidad': 2}
}

# Cálculo de utilidad esperada
def utilidad_esperada(opciones):
    resultado = {}
    for opcion, datos in opciones.items():
        utilidad = datos['probabilidad'] * datos['utilidad']
        resultado[opcion] = round(utilidad, 2)
    return resultado

# Elegir la mejor opción
def mejor_opcion(utilidades):
    return max(utilidades.items(), key=lambda x: x[1])

# Ejecutar modelo
utilidades = utilidad_esperada(opciones)
mejor = mejor_opcion(utilidades)

# Mostrar resultados
print("[Modelo Probabilista Racional - Decisión]")
for opcion, valor in utilidades.items():
    print(f"{opcion.replace('_', ' ').capitalize()}: utilidad esperada = {valor}")
print(f"\n→ Mejor decisión: {mejor[0].replace('_', ' ').capitalize()} (valor: {mejor[1]})")
