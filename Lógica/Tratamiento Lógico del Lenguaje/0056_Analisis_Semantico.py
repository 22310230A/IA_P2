# Análisis Semántico con ciudades de México

# Cada ciudad tiene un tipo asignado
tipos_ciudades = {
    'cdmx': 'urbana',
    'queretaro': 'urbana',
    'puebla': 'urbana',
    'veracruz': 'puerto',
    'san_luis': 'industrial',
    'monterrey': 'industrial',
    'guadalajara': 'urbana'
}

# Grafo de trayectos posibles
grafo = {
    'cdmx': ['queretaro', 'puebla'],
    'queretaro': ['san_luis'],
    'puebla': ['veracruz'],
    'san_luis': ['monterrey'],
    'veracruz': ['monterrey'],
    'monterrey': ['guadalajara'],
    'guadalajara': []
}

# Regla semántica:
# Se permite transitar si se va de:
# - urbana a urbana o industrial
# - industrial a urbana
# - puerto a industrial
# Cualquier otro trayecto es inválido.

def es_valido(origen, destino):
    tipo_origen = tipos_ciudades.get(origen, 'desconocido')
    tipo_destino = tipos_ciudades.get(destino, 'desconocido')

    if tipo_origen == 'urbana' and tipo_destino in ['urbana', 'industrial']:
        return True
    elif tipo_origen == 'industrial' and tipo_destino == 'urbana':
        return True
    elif tipo_origen == 'puerto' and tipo_destino == 'industrial':
        return True
    else:
        return False

# Análisis de todos los trayectos del grafo
print("[Análisis Semántico - Trayectos entre ciudades]")
for ciudad in grafo:
    for destino in grafo[ciudad]:
        valido = es_valido(ciudad, destino)
        print(f"{ciudad} -> {destino} ({tipos_ciudades[ciudad]} -> {tipos_ciudades[destino]}) → {'Válido' if valido else 'Inválido'}")
