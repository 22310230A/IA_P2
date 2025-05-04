# Gramática Causal Definida – Ruta CDMX a Guadalajara

# Hechos: indica qué trayectos están disponibles
hechos = {
    'cdmx_a_queretaro': True,
    'queretaro_a_san_luis': True,
    'san_luis_a_monterrey': True,
    'monterrey_a_guadalajara': True
}

# Reglas causales:
# Si se cumplen ciertas rutas, se deduce que se puede llegar a Guadalajara
reglas = [
    (
        ['cdmx_a_queretaro', 'queretaro_a_san_luis', 'san_luis_a_monterrey', 'monterrey_a_guadalajara'],
        'llegada_exitosa_a_guadalajara'
    ),
    (
        ['cdmx_a_queretaro', 'no_queretaro_a_san_luis'],
        'ruta_bloqueada_en_queretaro'
    ),
    (
        ['san_luis_a_monterrey', 'no_monterrey_a_guadalajara'],
        'sin_acceso_a_guadalajara'
    )
]

def aplicar_reglas(hechos, reglas):
    efectos = set()

    for causas, efecto in reglas:
        cumple = True
        for causa in causas:
            if causa.startswith("no_"):
                if hechos.get(causa[3:], False):
                    cumple = False
                    break
            elif not hechos.get(causa, False):
                cumple = False
                break
        if cumple:
            efectos.add(efecto)
    
    return efectos

# Aplicar reglas
efectos_derivados = aplicar_reglas(hechos, reglas)

# Mostrar resultados
print("[Gramática Causal Definida - Ruta CDMX a GDL]")
print("Hechos actuales:")
for k, v in hechos.items():
    print(f"- {k.replace('_', ' ')}: {'Sí' if v else 'No'}")

print("\nEfectos deducidos:")
for efecto in efectos_derivados:
    print(f"- {efecto.replace('_', ' ')}")
