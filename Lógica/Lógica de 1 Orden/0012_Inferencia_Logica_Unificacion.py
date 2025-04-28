# Inferencia Lógica: Unificación
#
# Simulamos el proceso de unificación de dos expresiones lógicas
# basadas en viajes entre estados de México.

# Función de unificación básica
def unificar(exp1, exp2):
    sustituciones = {}
    
    if len(exp1) != len(exp2):
        return None
    
    for t1, t2 in zip(exp1, exp2):
        if t1 == t2:
            continue
        elif t1.islower():  # t1 es variable
            sustituciones[t1] = t2
        elif t2.islower():  # t2 es variable
            sustituciones[t2] = t1
        else:
            return None  # No se pueden unificar si son constantes diferentes

    return sustituciones

# =========================
# EJEMPLO: VIAJES ENTRE CIUDADES
# =========================

# Unificamos viajes de una ciudad a otra
expresion1 = ['viaja', 'X', 'Querétaro']
expresion2 = ['viaja', 'alejandro', 'Querétaro']

# Realizar unificación
resultado = unificar(expresion1, expresion2)

print("[Inferencia Lógica: Unificación - Estilo Estados de México]")
print(f"Expresión 1: {expresion1}")
print(f"Expresión 2: {expresion2}")
if resultado is not None:
    print(f"Sustituciones necesarias para unificar: {resultado}\n")
else:
    print("No es posible unificar las expresiones.")

# Otro ejemplo
expresion3 = ['viaja', 'X', 'Guadalajara']
expresion4 = ['viaja', 'alejandro', 'Guadalajara']

resultado2 = unificar(expresion3, expresion4)

print(f"Expresión 3: {expresion3}")
print(f"Expresión 4: {expresion4}")
if resultado2 is not None:
    print(f"Sustituciones necesarias para unificar: {resultado2}")
else:
    print("No es posible unificar las expresiones.")
