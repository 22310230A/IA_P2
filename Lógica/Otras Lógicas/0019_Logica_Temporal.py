# Lógica Temporal
#
# Simulamos la evolución de un viaje entre ciudades a través del tiempo,
# aplicando operadores de lógica temporal: "finalmente" y "siempre".

# Línea temporal de estados (día a día del viaje)
# Cada día indica en qué ciudad está el agente
linea_tiempo = [
    'mexico',      # Día 1
    'queretaro',   # Día 2
    'san_luis',    # Día 3
    'guadalajara'  # Día 4
]

# Función para evaluar "finalmente en ciudad" (◇)
def finalmente(ciudad):
    return ciudad in linea_tiempo

# Función para evaluar "siempre en ciudad" (□)
def siempre(ciudad):
    return all(estacion == ciudad for estacion in linea_tiempo)

# Consultas
consultas = ['mexico', 'queretaro', 'guadalajara', 'zacatecas']

print("[Lógica Temporal - Viajes en el Tiempo]")
for ciudad in consultas:
    print(f"Ciudad consultada: {ciudad}")
    print(f"  ¿Finalmente llegó a {ciudad}? {'Sí' if finalmente(ciudad) else 'No'}")
    print(f"  ¿Siempre estuvo en {ciudad}? {'Sí' if siempre(ciudad) else 'No'}\n")
