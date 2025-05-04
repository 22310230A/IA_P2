# Inducción Gramatical – Ejemplo con rutas entre ciudades mexicanas

# Trayectos observados (como si fueran "frases" del lenguaje)
trayectos = [
    ['cdmx', 'queretaro', 'san_luis', 'guadalajara'],
    ['cdmx', 'puebla', 'veracruz', 'guadalajara'],
    ['cdmx', 'queretaro', 'san_luis'],
    ['cdmx', 'puebla', 'veracruz']
]

# Objetivo: inducir una gramática que describa cómo se puede llegar a Guadalajara

def inducir_gramatica(trayectos):
    reglas = set()
    for trayecto in trayectos:
        if 'guadalajara' in trayecto:
            index = trayecto.index('guadalajara')
            camino = " → ".join(trayecto[:index])
            reglas.add(f"{camino} → guadalajara")
    return reglas

# Inducir reglas a partir de las rutas observadas
gramatica_inducida = inducir_gramatica(trayectos)

# Mostrar resultados
print("[Inducción Gramatical - Rutas hacia Guadalajara]")
print("Reglas aprendidas:")
for regla in gramatica_inducida:
    print(f"- {regla}")
