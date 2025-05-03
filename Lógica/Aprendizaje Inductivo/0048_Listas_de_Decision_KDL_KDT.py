# Listas de Decisión: K-DL y K-DT (ejemplo sencillo)
#
# Estas listas contienen condiciones secuenciales que se aplican una por una
# hasta que alguna clasifica el ejemplo.

# Datos: edad y promedio → ¿pasa el curso?
ejemplos = [
    {'edad': 14, 'promedio': 6.0, 'pasa': 'no'},
    {'edad': 15, 'promedio': 7.0, 'pasa': 'sí'},
    {'edad': 16, 'promedio': 5.5, 'pasa': 'no'},
    {'edad': 17, 'promedio': 8.5, 'pasa': 'sí'}
]

# Lista de reglas simulando KDL/KDT
reglas = [
    lambda e: 'sí' if e['promedio'] >= 7 else None,
    lambda e: 'sí' if e['edad'] >= 16 else None,
    lambda e: 'no'
]

# Función que evalúa cada regla en orden
def clasificar(ejemplo, reglas):
    for regla in reglas:
        resultado = regla(ejemplo)
        if resultado is not None:
            return resultado
    return 'indefinido'

# Prueba de predicción
entrada = {'edad': 15, 'promedio': 6.5}
respuesta = clasificar(entrada, reglas)

print("[Listas de Decisión - KDL / KDT]")
print("Entrada:", entrada)
print("¿Pasa?:", respuesta)
