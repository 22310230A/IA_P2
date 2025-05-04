# Ejemplo de Ambigüedad en Rutas entre Estados

# Supongamos que queremos llegar a Guadalajara (GDL)
# desde Ciudad de México (CDMX), y hay dos caminos posibles

# Hechos sobre rutas disponibles
hechos = {
    'cdmx_a_queretaro': True,
    'queretaro_a_san_luis': True,
    'san_luis_a_guadalajara': True,
    'cdmx_a_puebla': True,
    'puebla_a_veracruz': True,
    'veracruz_a_guadalajara': True
}

# Interpretaciones posibles de cómo llegar a Guadalajara
interpretaciones = [
    ['cdmx_a_queretaro', 'queretaro_a_san_luis', 'san_luis_a_guadalajara'],
    ['cdmx_a_puebla', 'puebla_a_veracruz', 'veracruz_a_guadalajara']
]

def evaluar_rutas(hechos, interpretaciones):
    rutas_validas = []
    for ruta in interpretaciones:
        if all(hechos.get(paso, False) for paso in ruta):
            rutas_validas.append(ruta)
    return rutas_validas

# Evaluar
rutas_posibles = evaluar_rutas(hechos, interpretaciones)

# Mostrar resultados
print("[Ambigüedad en rutas hacia Guadalajara]")
print("Rutas válidas encontradas:")
for i, ruta in enumerate(rutas_posibles, 1):
    ruta_texto = " → ".join([paso.replace('_a_', ' a ').upper() for paso in ruta])
    print(f"Ruta {i}: {ruta_texto}")
