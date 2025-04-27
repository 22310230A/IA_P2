# Resolución y Forma Normal Conjuntiva (FNC)
#
# Simulamos la conversión de una expresión lógica a FNC
# y aplicamos resolución para verificar satisfacibilidad.

# Operadores lógicos
def implica(p, q):
    return not p or q

# Simulación manual:
# Ejemplo: (p ⇒ q) es equivalente a (¬p ∨ q)
# FNC: ya está en forma de disyunción (OR) de literales

# Definimos cláusulas en forma de listas (simulando FNC)
# Ejemplo: (¬p ∨ q) se representa como [-p, q]
# Aquí representamos literales como strings: 'p', '¬p', 'q', etc.

base_fnc = [
    ['¬p', 'q'],   # (¬p ∨ q)
    ['p'],         # p
    ['¬q']         # ¬q
]

# Función de resolución entre dos cláusulas
def resolver(cl1, cl2):
    for literal in cl1:
        if ('¬' + literal) in cl2 or (literal[1:] if literal.startswith('¬') else '¬' + literal) in cl2:
            nueva_clausula = set(cl1 + cl2)
            # Eliminar el literal y su negación
            nueva_clausula.discard(literal)
            nueva_clausula.discard(('¬' + literal) if not literal.startswith('¬') else literal[1:])
            return list(nueva_clausula)
    return None

# Aplicar resolución
def aplicar_resolucion(base):
    nueva = base.copy()
    while True:
        nuevas_clausulas = []
        for i in range(len(nueva)):
            for j in range(i + 1, len(nueva)):
                resolvente = resolver(nueva[i], nueva[j])
                if resolvente == []:  # Clausula vacía => contradicción encontrada
                    return True
                if resolvente and resolvente not in nueva and resolvente not in nuevas_clausulas:
                    nuevas_clausulas.append(resolvente)
        if not nuevas_clausulas:
            return False
        nueva.extend(nuevas_clausulas)

# Resultado
resultado = aplicar_resolucion(base_fnc)

print("[Resolución y Forma Normal Conjuntiva (FNC)]")
print(f"¿La base lleva a contradicción (insatisfacible)? {'Sí' if resultado else 'No'}")
