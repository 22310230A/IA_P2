# Traducción Automática Estadística
#
# Simulamos un sistema básico de traducción automática basado en conteo de frases y frecuencias.

from collections import Counter

# Corpus de entrenamiento: pares frase_origen -> frase_destino
corpus_paralelo = [
    ("quiero viajar", "i want to travel"),
    ("quiero comer", "i want to eat"),
    ("me gusta viajar", "i like to travel"),
    ("me gusta comer", "i like to eat"),
    ("viajar es divertido", "traveling is fun")
]

# Construimos una tabla de traducción (simplemente conteo)
tabla_traduccion = Counter()

for origen, destino in corpus_paralelo:
    tabla_traduccion[origen] = destino

# Función de traducción simple
def traducir(frase):
    if frase in tabla_traduccion:
        return tabla_traduccion[frase]
    else:
        return "Traducción desconocida"

# Ejemplos de traducción
frases_a_traducir = [
    "quiero viajar",
    "me gusta comer",
    "viajar es divertido",
    "quiero aprender"
]

print("[Traducción Automática Estadística]")
for frase in frases_a_traducir:
    traduccion = traducir(frase)
    print(f"{frase} -> {traduccion}")
