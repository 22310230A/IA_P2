# Lógica Proposicional: Sintaxis y Semántica - Tablas de Verdad
#
# Creamos una tabla de verdad para dos proposiciones p y q
# con los conectivos: AND, OR, NOT, IMPLICA, BICONDICIONAL.

import itertools

# Definir operadores lógicos
def implica(p, q):
    return not p or q

def bicondicional(p, q):
    return (p and q) or (not p and not q)

# Todas las combinaciones posibles de verdad/falsedad para p y q
valores = list(itertools.product([True, False], repeat=2))

# Encabezado de la tabla
print("[Tabla de Verdad]")
print(f"{'p':<6}{'q':<6}{'¬p':<6}{'p∧q':<6}{'p∨q':<6}{'p⇒q':<6}{'p⇔q':<6}")
print("-" * 40)

# Construir la tabla
for p, q in valores:
    not_p = not p
    p_and_q = p and q
    p_or_q = p or q
    p_implica_q = implica(p, q)
    p_bicondicional_q = bicondicional(p, q)
    
    print(f"{str(p):<6}{str(q):<6}{str(not_p):<6}{str(p_and_q):<6}{str(p_or_q):<6}{str(p_implica_q):<6}{str(p_bicondicional_q):<6}")
