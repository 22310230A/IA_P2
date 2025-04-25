# Modelo Probabilístico del Lenguaje: Corpus
#
# Un modelo probabilístico de lenguaje asigna probabilidades a secuencias de palabras,
# basándose en un corpus de ejemplos reales.

import matplotlib
matplotlib.use('TkAgg')

from collections import Counter
import matplotlib.pyplot as plt

# Corpus simple de ejemplo
corpus = [
    "quiero viajar a guadalajara",
    "quiero comer en querétaro",
    "viajar es divertido",
    "comer en guadalajara es delicioso",
    "querétaro tiene buena comida"
]

# Preprocesar: separar palabras
palabras = []
for frase in corpus:
    palabras.extend(frase.split())

# Contar frecuencia de palabras
conteo_palabras = Counter(palabras)

# Calcular probabilidad de cada palabra
total_palabras = sum(conteo_palabras.values())
probabilidades = {palabra: freq / total_palabras for palabra, freq in conteo_palabras.items()}

# Mostrar resultados
print("[Modelo Probabilístico del Lenguaje - Corpus]")
print("Probabilidades de cada palabra:\n")
for palabra, prob in sorted(probabilidades.items(), key=lambda x: -x[1]):
    print(f"{palabra}: {prob:.4f}")

# Graficar distribución
plt.figure(figsize=(10, 5))
plt.bar(probabilidades.keys(), probabilidades.values())
plt.title("Distribución de Probabilidades del Corpus")
plt.ylabel("Probabilidad")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
