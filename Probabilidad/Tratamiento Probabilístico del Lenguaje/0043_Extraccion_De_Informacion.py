# Extracción de Información
#
# Simulamos un sistema que extrae entidades específicas (lugares, acciones)
# de un conjunto de frases.

import re

# Corpus de frases
corpus = [
    "quiero viajar a guadalajara",
    "me gustaría comer en querétaro",
    "viajar a zacatecas es una gran experiencia",
    "comer en guadalajara es delicioso"
]

# Definimos patrones para extracción
patron_lugares = r"\ba\s+(\w+)|en\s+(\w+)"  # palabras después de "a" o "en"
patron_acciones = r"\b(quiero|gustaría|viajar|comer)\b"  # verbos principales

# Función de extracción
def extraer_info(frases):
    lugares = []
    acciones = []
    for frase in frases:
        lugares_encontrados = re.findall(patron_lugares, frase)
        acciones_encontradas = re.findall(patron_acciones, frase)
        
        # Limpiar resultados
        for par in lugares_encontrados:
            lugar = par[0] if par[0] else par[1]
            lugares.append(lugar)
        acciones.extend(acciones_encontradas)
    return lugares, acciones

# Ejecutar extracción
lugares, acciones = extraer_info(corpus)

# Mostrar resultados
print("[Extracción de Información]")
print("\nLugares encontrados:")
for lugar in lugares:
    print(f"  - {lugar}")

print("\nAcciones encontradas:")
for accion in acciones:
    print(f"  - {accion}")
