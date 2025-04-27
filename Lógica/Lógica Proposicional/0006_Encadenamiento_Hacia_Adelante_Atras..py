# Encadenamiento: Hacia Adelante y Hacia Atrás
#
# Simulamos los dos métodos básicos de inferencia en lógica:
# - Encadenamiento hacia adelante: partir de hechos conocidos y aplicar reglas.
# - Encadenamiento hacia atrás: partir de una meta y buscar hechos que la justifiquen.

# ===============================
# PRIMER EJEMPLO
# ===============================

# Base de conocimiento: reglas y hechos
reglas = {
    'p': [],
    'p⇒q': ['p'],
    'q⇒r': ['q']
}

# Hechos iniciales
hechos = {'p'}

# Función de encadenamiento hacia adelante
def encadenar_adelante(hechos, reglas, meta):
    nuevos = hechos.copy()
    cambio = True
    while cambio:
        cambio = False
        for regla, condiciones in reglas.items():
            if regla not in nuevos and all(c in nuevos for c in condiciones):
                nuevos.add(regla)
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

# Ejecutar primer ejemplo
meta = 'r'
resultado_adelante = encadenar_adelante(hechos, reglas, meta)
resultado_atras = encadenar_atras(hechos, reglas, meta)

# Mostrar resultados primer ejemplo
print("[Encadenamiento Hacia Adelante y Atrás - Ejemplo 1]")
print(f"¿Meta '{meta}' alcanzable por encadenamiento hacia adelante? {'Sí' if resultado_adelante else 'No'}")
print(f"¿Meta '{meta}' alcanzable por encadenamiento hacia atrás? {'Sí' if resultado_atras else 'No'}\n")

# ===============================
# SEGUNDO EJEMPLO
# ===============================

# Nuevo conjunto de reglas y hechos
reglas2 = {
    'tiene_ala(pajaro)': [],
    'tiene_pico(pajaro)': [],
    'puede_volar(X)': ['tiene_ala(X)', 'tiene_pico(X)']
}

hechos2 = {'tiene_ala(pajaro)', 'tiene_pico(pajaro)'}

# Nueva meta
meta2 = 'puede_volar(pajaro)'

# Ejecutar segundo ejemplo
resultado_adelante2 = encadenar_adelante(hechos2, reglas2, meta2)
resultado_atras2 = encadenar_atras(hechos2, reglas2, meta2)

# Mostrar resultados segundo ejemplo
print("[Encadenamiento Hacia Adelante y Atrás - Ejemplo 2]")
print(f"¿Meta '{meta2}' alcanzable por encadenamiento hacia adelante? {'Sí' if resultado_adelante2 else 'No'}")
print(f"¿Meta '{meta2}' alcanzable por encadenamiento hacia atrás? {'Sí' if resultado_atras2 else 'No'}")
