# Acciones, Situaciones y Eventos: Marcos
#
# Simulamos el uso de marcos (frames) para representar situaciones
# como eventos estructurados con atributos.

# Definición de un marco: "viaje"
marco_viaje = {
    'evento': 'viaje',
    'origen': 'CDMX',
    'destino': 'Guadalajara',
    'medio': 'camión',
    'duracion': '6 horas',
    'estado': 'completado'
}

# Otro marco: "reunión"
marco_reunion = {
    'evento': 'reunión',
    'lugar': 'Querétaro',
    'tema': 'automatización industrial',
    'participantes': ['Alejandro', 'Julio'],
    'hora': '10:00 AM'
}

# Función para mostrar un marco
def mostrar_marco(marco):
    print(f"--- {marco['evento'].capitalize()} ---")
    for clave, valor in marco.items():
        if clave != 'evento':
            print(f"{clave.capitalize()}: {valor}")
    print()

# Mostrar marcos
print("[Acciones, Situaciones y Eventos - Marcos]\n")
mostrar_marco(marco_viaje)
mostrar_marco(marco_reunion)
