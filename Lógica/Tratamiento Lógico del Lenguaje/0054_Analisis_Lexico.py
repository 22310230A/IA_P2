# Análisis Léxico
#
# Este script simula un analizador léxico muy básico,
# separando palabras y clasificándolas como identificadores, números o símbolos.

import re

def analizar_lexico(texto):
    tokens = texto.split()
    resultado = []

    for token in tokens:
        if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token):
            resultado.append((token, "Identificador"))
        elif re.match(r'^\d+(\.\d+)?$', token):
            resultado.append((token, "Número"))
        elif token in ['+', '-', '*', '/', '=', '(', ')']:
            resultado.append((token, "Símbolo"))
        else:
            resultado.append((token, "Desconocido"))
    
    return resultado

# Texto de prueba
entrada = "total = valor1 + 25"

tokens_clasificados = analizar_lexico(entrada)

print("[Análisis Léxico]")
print("Entrada:", entrada)
print("Tokens clasificados:")
for token, tipo in tokens_clasificados:
    print(f"- {token}: {tipo}")
