# Ingeniería del Conocimiento
#
# Simulamos la construcción de una base de conocimiento estructurada
# con hechos y reglas para poder consultar información de manera lógica.

# Base de conocimiento: hechos y reglas
hechos = {
    'es_animal(perro)': True,
    'es_animal(gato)': True,
    'es_mascota(perro)': True,
    'es_domestico(gato)': True
}

reglas = {
    'es_mascota(X)': ['es_animal(X)', 'es_domestico(X)']
}

# Función de consulta simple basada en la base de conocimiento
def consultar(hecho):
    if hecho in hechos:
        return hechos[hecho]
    for regla, condiciones in reglas.items():
        if hecho.split('(')[0] == regla.split('(')[0]:
            variable = hecho.split('(')[1].strip(')')
            condiciones_instanciadas = [cond.replace('X', variable) for cond in condiciones]
            if all(consultar(c) for c in condiciones_instanciadas):
                return True
    return False

# Ejemplos de consulta
consultas = [
    'es_mascota(perro)',
    'es_mascota(gato)',
    'es_domestico(perro)'
]

# Mostrar resultados
print("[Ingeniería del Conocimiento]")
for consulta in consultas:
    resultado = consultar(consulta)
    print(f"Consulta: {consulta} => {'Verdadero' if resultado else 'Falso'}")
