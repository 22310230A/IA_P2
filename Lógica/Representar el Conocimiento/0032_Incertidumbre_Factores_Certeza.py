# Incertidumbre y Factores de Certeza
#
# Simulamos cómo representar conocimiento con grados de certeza (valores entre -1 y 1).

# Base de reglas con factores de certeza (FC)
# FC positivo = certeza; FC negativo = certeza en la negación; 0 = desconocido
factores_certeza = {
    'llueve_en(queretaro)': 0.8,
    'hay_trafico_en(cdmx)': 1.0,
    'hay_trafico_en(guadalajara)': 0.3,
    'viajar_a(zacatecas)': -0.6  # significa que probablemente NO se debe viajar a Zacatecas
}

# Función para interpretar FC
def interpretar_fc(proposicion):
    fc = factores_certeza.get(proposicion, 0)
    if fc == 0:
        return "No se tiene evidencia."
    elif fc > 0.7:
        return f"Alta certeza de que {proposicion.replace('_', ' ')}."
    elif fc > 0:
        return f"Posible que {proposicion.replace('_', ' ')}."
    elif fc < -0.7:
        return f"Alta certeza de que NO {proposicion.replace('_', ' ')}."
    else:
        return f"Probablemente NO {proposicion.replace('_', ' ')}."

# Consultas
consultas = [
    'llueve_en(queretaro)',
    'hay_trafico_en(cdmx)',
    'hay_trafico_en(guadalajara)',
    'viajar_a(zacatecas)',
    'viajar_a(queretaro)'
]

print("[Incertidumbre y Factores de Certeza]\n")
for prop in consultas:
    print(f"{prop}: {interpretar_fc(prop)}")
