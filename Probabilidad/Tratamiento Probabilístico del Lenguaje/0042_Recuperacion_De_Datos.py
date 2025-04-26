# Recuperación de Datos
#
# Simulamos un motor de búsqueda sencillo que encuentra frases relevantes
# en un corpus basado en coincidencias de palabras clave.

from collections import defaultdict

# Corpus simple de frases
corpus = [
    "quiero viajar a guadalajara",
    "comer en querétaro es delicioso",
    "la comida en guadalajara es muy buena",
    "me gustaría viajar a zacatecas",
    "la gastronomía de querétaro es excelente"
]

# Índice invertido: palabra -> lista de frases donde aparece
indice_invertido = defaultdict(list)

for idx, frase in enumerate(corpus):
    palabras = frase.split()
    for palabra in palabras:
        indice_invertido[palabra].append(idx)

# Función de recuperación
def buscar(palabra_clave):
    if palabra_clave in indice_invertido:
        indices = indice_invertido[palabra_clave]
        return [corpus[i] for i in indices]
    else:
        return []

# Ejemplos de búsqueda
print("[Recuperación de Datos]")

consultas = ['guadalajara', 'querétaro', 'viajar', 'comida']

for consulta in consultas:
    resultados = buscar(consulta)
    print(f"\nConsulta: {consulta}")
    for r in resultados:
        print(f"  Resultado: {r}")
