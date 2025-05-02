# Razonamiento por Defecto y No Monotónico
#
# Simulamos un sistema donde se asumen cosas por defecto,
# pero esas conclusiones pueden cambiar con nueva información.

# Base de hechos conocidos
hechos = {
    'es_ciudad(queretaro)': True,
    'es_ciudad(zacatecas)': True
}

# Hechos por defecto
por_defecto = {
    'tiene_transporte_publico(queretaro)': True,
    'tiene_transporte_publico(zacatecas)': True
}

# Excepciones añadidas luego (nueva información)
excepciones = {
    'tiene_transporte_publico(zacatecas)': False  # nuevo hecho contradice el defecto
}

# Función de razonamiento por defecto
def razonamiento(ciudad):
    if ciudad in excepciones:
        return excepciones[ciudad]
    return por_defecto.get(f'tiene_transporte_publico({ciudad})', None)

# Consultas
ciudades = ['queretaro', 'zacatecas']

print("[Razonamiento por Defecto y No Monotónico]\n")
for c in ciudades:
    resultado = razonamiento(c)
    if resultado is True:
        print(f"Se asume que {c.capitalize()} tiene transporte público.")
    elif resultado is False:
        print(f"Se sabe que {c.capitalize()} no tiene transporte público.")
    else:
        print(f"No se tiene información suficiente sobre {c.capitalize()}.")
