# Agentes Lógicos
#
# Simulamos un agente que razona basándose en reglas lógicas
# para decidir cómo moverse entre estados (ciudades).

# Base de conocimiento: conexiones entre ciudades
conexiones = {
    'mexico': ['queretaro'],
    'queretaro': ['san_luis'],
    'san_luis': ['guadalajara']
}

# Definimos el "agente" como una función que razona para alcanzar un destino
def agente_logico(origen, destino, visitados=None):
    if visitados is None:
        visitados = set()
    if origen == destino:
        return True
    visitados.add(origen)
    for siguiente in conexiones.get(origen, []):
        if siguiente not in visitados:
            if agente_logico(siguiente, destino, visitados):
                return True
    return False

# Ejemplos de consulta
print("[Agentes Lógicos]")

# ¿Puede el agente llegar de México a Guadalajara?
resultado1 = agente_logico('mexico', 'guadalajara')
print(f"¿Puede el agente llegar de México a Guadalajara? {'Sí' if resultado1 else 'No'}")

# ¿Puede el agente llegar de Querétaro a México? (No, porque no hay conexión de regreso)
resultado2 = agente_logico('queretaro', 'mexico')
print(f"¿Puede el agente llegar de Querétaro a México? {'Sí' if resultado2 else 'No'}")
