# Programación Lógica: Prolog y CLIPS
#
# Simulamos cómo sería una pequeña base de conocimiento
# y consultas típicas inspiradas en Prolog o CLIPS.

# Definimos hechos como base de conocimiento
base_conocimiento = {
    'viaja(mexico, queretaro)': True,
    'viaja(queretaro, san_luis)': True,
    'viaja(san_luis, guadalajara)': True
}

# Función de consulta tipo Prolog: ¿hay una conexión directa?
def consulta_conexion(origen, destino):
    hecho = f'viaja({origen}, {destino})'
    return base_conocimiento.get(hecho, False)

# Función para consulta tipo encadenamiento: ¿puedo llegar desde origen a destino?
def puede_llegar(origen, destino, visitados=None):
    if visitados is None:
        visitados = set()
    if origen == destino:
        return True
    visitados.add(origen)
    for hecho in base_conocimiento:
        if hecho.startswith(f'viaja({origen},'):
            siguiente = hecho.split(',')[1].strip(')')
            if siguiente not in visitados and puede_llegar(siguiente, destino, visitados):
                return True
    return False

# Consultas de ejemplo
print("[Programación Lógica: Prolog y CLIPS]")

# Consulta directa
print(f"¿Existe un viaje directo de México a Querétaro? {'Sí' if consulta_conexion('mexico', 'queretaro') else 'No'}")

# Consulta indirecta (encadenada)
print(f"¿Se puede llegar de México a Guadalajara? {'Sí' if puede_llegar('mexico', 'guadalajara') else 'No'}")

# Caso imposible
print(f"¿Se puede llegar de Querétaro a México? {'Sí' if puede_llegar('queretaro', 'mexico') else 'No'}")
