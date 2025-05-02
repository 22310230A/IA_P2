# Reglas, Redes Semánticas y Lógica Descriptiva
#
# Simulamos una red semántica con relaciones entre conceptos
# y reglas que permiten inferir conocimiento.

# Red semántica: nodos y relaciones (tipo sujeto-verbo-objeto)
relaciones = [
    ('cdmx', 'es_parte_de', 'mexico'),
    ('queretaro', 'es_parte_de', 'mexico'),
    ('camion', 'es_un', 'transporte'),
    ('alejandro', 'viaja_en', 'camion'),
    ('alejandro', 'visita', 'queretaro')
]

# Función para buscar conexiones directas
def buscar_relacion(sujeto, verbo=None):
    resultados = []
    for s, v, o in relaciones:
        if s == sujeto and (verbo is None or v == verbo):
            resultados.append((v, o))
    return resultados

# Reglas descriptivas (informales)
def reglas_inferencia():
    print("→ Reglas de inferencia aplicadas:")
    for s, v, o in relaciones:
        if v == 'viaja_en':
            print(f"  {s.capitalize()} usa un medio de transporte: {o}")
        if v == 'visita':
            print(f"  {s.capitalize()} estuvo en {o.capitalize()}")
        if v == 'es_parte_de' and o == 'mexico':
            print(f"  {s.capitalize()} es una ciudad mexicana.")

# Mostrar red y reglas
print("[Reglas, Redes Semánticas y Lógica Descriptiva]\n")

entidad = 'alejandro'
conexiones = buscar_relacion(entidad)
print(f"Relaciones directas de '{entidad}':")
for v, o in conexiones:
    print(f"  {entidad} {v.replace('_', ' ')} {o}")

print()
reglas_inferencia()
