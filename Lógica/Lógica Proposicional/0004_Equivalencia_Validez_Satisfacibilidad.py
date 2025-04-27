# Equivalencia, Validez y Satisfacibilidad
#
# Comprobamos si dos expresiones lógicas son equivalentes
# y verificamos validez o satisfacibilidad mediante tablas de verdad.

import itertools

# Definimos operadores lógicos
def implica(p, q):
    return not p or q

def equivalentes(expr1, expr2):
    # Comprobamos equivalencia evaluando todas las combinaciones
    valores = list(itertools.product([True, False], repeat=2))
    for p, q in valores:
        if expr1(p, q) != expr2(p, q):
            return False
    return True

# Expresiones a comparar
# (p ⇒ q) ≡ (¬p ∨ q)
def expr1(p, q):
    return implica(p, q)

def expr2(p, q):
    return (not p) or q

# Verificación de equivalencia
es_equivalente = equivalentes(expr1, expr2)

# Verificación de validez (¿siempre verdadero?)
def es_valida(expr):
    valores = list(itertools.product([True, False], repeat=2))
    for p, q in valores:
        if not expr(p, q):
            return False
    return True

# Verificación de satisfacibilidad (¿alguna vez verdadero?)
def es_satisfacible(expr):
    valores = list(itertools.product([True, False], repeat=2))
    for p, q in valores:
        if expr(p, q):
            return True
    return False

# Resultados
print("[Equivalencia, Validez y Satisfacibilidad]")
print(f"¿Son equivalentes (p⇒q) y (¬p∨q)? {'Sí' if es_equivalente else 'No'}")
print(f"¿La expresión (p⇒q) es válida? {'Sí' if es_valida(expr1) else 'No'}")
print(f"¿La expresión (p⇒q) es satisfacible? {'Sí' if es_satisfacible(expr1) else 'No'}")
