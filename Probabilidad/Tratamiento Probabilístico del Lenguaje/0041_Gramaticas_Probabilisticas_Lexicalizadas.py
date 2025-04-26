# Gramáticas Probabilísticas Lexicalizadas
#
# Las gramáticas probabilísticas lexicalizadas asocian palabras específicas
# (lexemas) a los símbolos de las reglas, refinando la generación.

import random

# Definimos una gramática lexicalizada simple
gramatica_lex = {
    'S': [('NP VP', 1.0)],
    'NP': [('yo/viajero', 0.5), ('tú/comensal', 0.5)],
    'VP': [('quiero/viajar', 0.5), ('quieres/comer', 0.5)]
}

# Función para expandir un símbolo
def expandir_lex(simbolo):
    if simbolo not in gramatica_lex:
        palabra, etiqueta = simbolo.split('/')
        return palabra  # Tomamos solo el lexema (palabra)
    producciones = gramatica_lex[simbolo]
    reglas, probs = zip(*producciones)
    seleccion = random.choices(reglas, weights=probs)[0]
    return ' '.join(expandir_lex(p) for p in seleccion.split())

# Generar frases lexicalizadas
print("[Gramáticas Probabilísticas Lexicalizadas]")
for _ in range(5):
    frase = expandir_lex('S')
    print(f"Frase generada: {frase}")
