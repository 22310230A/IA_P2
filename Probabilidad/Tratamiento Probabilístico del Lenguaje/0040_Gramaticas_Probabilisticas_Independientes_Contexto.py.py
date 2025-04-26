# Gramáticas Probabilísticas Independientes del Contexto (PCFG)
#
# Una PCFG asigna probabilidades a las reglas de producción
# para generar oraciones de manera controlada por probabilidades.

import random

# Definimos una gramática simple con probabilidades
gramatica = {
    'S': [('NP VP', 1.0)],
    'NP': [('yo', 0.5), ('tú', 0.5)],
    'VP': [('quiero viajar', 0.5), ('quieres comer', 0.5)]
}

# Función para expandir un símbolo
def expandir(simbolo):
    if simbolo not in gramatica:
        return simbolo  # símbolo terminal
    producciones = gramatica[simbolo]
    reglas, probs = zip(*producciones)
    seleccion = random.choices(reglas, weights=probs)[0]
    return ' '.join(expandir(p) for p in seleccion.split())

# Generar frases
print("[Gramáticas Probabilísticas Independientes del Contexto]")
for _ in range(5):
    frase = expandir('S')
    print(f"Frase generada: {frase}")
