# Gramáticas: Jerarquía de Chomsky

# Este código clasifica una gramática dada en la jerarquía de Chomsky
# de forma muy básica y solo con fines didácticos.

def clasificar_gramatica(producciones):
    es_tipo3 = True
    es_tipo2 = True

    for produccion in producciones:
        izquierda, derecha = produccion.split('->')
        izquierda = izquierda.strip()
        derecha = derecha.strip()

        if len(izquierda) != 1 or not izquierda.isupper():
            es_tipo2 = False
            es_tipo3 = False
        if not (derecha.islower() or (len(derecha) == 2 and derecha[0].islower() and derecha[1].isupper())):
            es_tipo3 = False

    if es_tipo3:
        return "Tipo 3: Gramática Regular"
    elif es_tipo2:
        return "Tipo 2: Gramática Libre de Contexto"
    else:
        return "Tipo 1 o 0: Más compleja"

# Ejemplo de gramática simple
producciones = [
    "S -> aA",
    "A -> bB",
    "B -> c"
]

tipo = clasificar_gramatica(producciones)

print("[Gramáticas - Jerarquía de Chomsky]")
print("Producciones:", producciones)
print("Clasificación:", tipo)
