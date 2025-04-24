# Naïve Bayes
#
# Es un clasificador probabilístico que asume que las características
# son independientes entre sí dado el resultado.
#
# Usaremos un ejemplo con dos clases: 'Compra' o 'No Compra'
# y características: edad (joven, adulto) y ingreso (bajo, alto)

from collections import Counter

# Datos de entrenamiento
datos = [
    {'edad': 'joven', 'ingreso': 'alto', 'clase': 'No Compra'},
    {'edad': 'joven', 'ingreso': 'alto', 'clase': 'No Compra'},
    {'edad': 'adulto', 'ingreso': 'alto', 'clase': 'Compra'},
    {'edad': 'adulto', 'ingreso': 'bajo', 'clase': 'Compra'},
    {'edad': 'adulto', 'ingreso': 'bajo', 'clase': 'Compra'},
    {'edad': 'joven', 'ingreso': 'bajo', 'clase': 'No Compra'}
]

# Función para contar ocurrencias
def contar_ocurrencias(datos, atributo, valor, clase):
    return sum(1 for d in datos if d[atributo] == valor and d['clase'] == clase)

# Clasificador Naïve Bayes
def naive_bayes(observacion, datos):
    clases = list(set(d['clase'] for d in datos))
    total = len(datos)
    resultados = {}

    for c in clases:
        prob_clase = sum(1 for d in datos if d['clase'] == c) / total
        prob_atributos = 1.0
        for atributo in observacion:
            conteo = contar_ocurrencias(datos, atributo, observacion[atributo], c)
            total_clase = sum(1 for d in datos if d['clase'] == c)
            prob_atributos *= (conteo / total_clase) if total_clase > 0 else 0
        resultados[c] = prob_clase * prob_atributos

    # Normalizar (opcional)
    suma = sum(resultados.values())
    for c in resultados:
        resultados[c] /= suma if suma > 0 else 1

    return resultados

# Observación a clasificar
observacion = {'edad': 'joven', 'ingreso': 'bajo'}

# Ejecutar clasificación
resultados = naive_bayes(observacion, datos)

# Mostrar resultados
print("[Naïve Bayes]")
print(f"Observación: {observacion}")
for clase, prob in resultados.items():
    print(f"  P({clase}) = {prob:.4f}")
