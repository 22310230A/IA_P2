# Análisis Sintáctico
#
# Este analizador verifica si una expresión aritmética simple cumple con la sintaxis esperada.
# Utiliza una pila para validar el orden de los elementos.

import re

# Definir patrones de tokens
identificador = r'[a-zA-Z_][a-zA-Z0-9_]*'
numero = r'\d+'
operador = r'[\+\-\*/]'
parentesis = r'[\(\)]'
token_pattern = f'({identificador})|({numero})|({operador})|({parentesis})'

def es_valida(tokens):
    pila = []
    ultimo = ''
    for token in tokens:
        if token == '(':
            pila.append(token)
        elif token == ')':
            if not pila or pila[-1] != '(':
                return False
            pila.pop()
        elif re.match(operador, token):
            if ultimo == '' or re.match(operador, ultimo):
                return False
        ultimo = token
    return len(pila) == 0 and not re.match(operador, ultimo)

# Expresión de prueba
entrada = "x + ( y * 5 )"
tokens = re.findall(token_pattern, entrada)
tokens = [t for grupo in tokens for t in grupo if t]

print("[Análisis Sintáctico]")
print("Expresión:", entrada)
print("Tokens:", tokens)
print("¿Es válida?:", "Sí" if es_valida(tokens) else "No")
