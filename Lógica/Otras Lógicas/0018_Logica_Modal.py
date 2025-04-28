# Lógica Modal
#
# Simulamos conceptos básicos de lógica modal aplicados
# a viajes entre ciudades de México.

# Base de conocimiento: mundos posibles (escenarios de rutas)
mundos_viajes = {
    'mundo1': {'viaja_mexico_queretaro', 'viaja_queretaro_sanluis'},
    'mundo2': {'viaja_queretaro_sanluis', 'viaja_sanluis_guadalajara'},
    'mundo3': {'viaja_mexico_queretaro', 'viaja_sanluis_guadalajara'}
}

# Función para evaluar "necesariamente p" (□p)
def necesariamente(p):
    for mundo in mundos_viajes.values():
        if p not in mundo:
            return False
    return True

# Función para evaluar "posiblemente p" (◇p)
def posiblemente(p):
    for mundo in mundos_viajes.values():
        if p in mundo:
            return True
    return False

# Consultas
proposiciones = ['viaja_mexico_queretaro', 'viaja_queretaro_sanluis', 'viaja_mexico_guadalajara']

print("[Lógica Modal - Viajes entre Ciudades]")
for p in proposiciones:
    print(f"Proposición: {p}")
    print(f"  Necesariamente: {'Sí' if necesariamente(p) else 'No'}")
    print(f"  Posiblemente: {'Sí' if posiblemente(p) else 'No'}\n")
