# Encadenamiento: Hacia Adelante y Atrás
#
# Simulamos inferencia lógica usando encadenamiento
# en un ejemplo de viajes entre ciudades de México.

# Base de conocimiento: reglas
reglas = {
    'puede_viajar_a(queretaro)': ['puede_viajar_a(cdmx)'],
    'puede_viajar_a(san_luis)': ['puede_viajar_a(queretaro)'],
    'puede_viajar_a(guadalajara)': ['puede_viajar_a(san_luis)']
}

# Hechos conocidos
hechos = {'puede_viajar_a(cdmx)'}

# Función de encadenamiento hacia adelante
def encadenar_adelante(hechos, reglas, meta):
    nuevos = hechos.copy()
    cambio = True
    while cambio:
        cambio = False
        for conclusion, condiciones in reglas.items():
            if conclusion not in nuevos and all(c in nuevos for c in condiciones):
                nuevos.add(conclusion)
                cambio = True
    return meta in nuevos

# Función de encadenamiento hacia atrás
def encadenar_atras(hechos, reglas, meta):
    if meta in hechos:
        return True
    if meta in reglas:
        for condicion in reglas[meta]:
            if not encadenar_atras(hechos, reglas, condicion):
                return False
        return True
    return False

# Definimos la meta
meta = 'puede_viajar_a(guadalajara)'

# Ejecutar encadenamientos
resultado_adelante = encadenar_adelante(hechos, reglas, meta)
resultado_atras = encadenar_atras(hechos, reglas, meta)

# Mostrar resultados
print("[Encadenamiento Hacia Adelante y Atrás - Estados de México]")
print(f"¿Es posible llegar a Guadalajara partiendo de CDMX usando encadenamiento hacia adelante? {'Sí' if resultado_adelante else 'No'}")
print(f"¿Es posible llegar a Guadalajara partiendo de CDMX usando encadenamiento hacia atrás? {'Sí' if resultado_atras else 'No'}")
