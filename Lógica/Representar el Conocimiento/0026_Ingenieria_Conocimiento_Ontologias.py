# Ingeniería del Conocimiento: Ontologías
#
# Simulamos una ontología simple con clases, subclases y relaciones
# entre conceptos dentro de un dominio: ciudades y medios de transporte.

# Ontología como estructura jerárquica
ontologia = {
    'Transporte': ['Terrestre', 'Aéreo'],
    'Terrestre': ['Camión', 'Auto'],
    'Aéreo': ['Avión'],
    'Ciudad': ['CDMX', 'Querétaro', 'Guadalajara'],
    'Ubicacion': ['Ciudad'],
    'Medio': ['Transporte']
}

# Relaciones (instancias)
instancias = {
    'Camión': {'tipo': 'Terrestre', 'capacidad': 40},
    'Auto': {'tipo': 'Terrestre', 'capacidad': 5},
    'Avión': {'tipo': 'Aéreo', 'capacidad': 180},
    'CDMX': {'tipo': 'Ciudad', 'estado': 'Valle de México'},
    'Querétaro': {'tipo': 'Ciudad', 'estado': 'Querétaro'},
    'Guadalajara': {'tipo': 'Ciudad', 'estado': 'Jalisco'}
}

# Función para explorar jerarquías
def obtener_subclases(clase):
    return ontologia.get(clase, [])

# Función para consultar propiedades de una instancia
def obtener_info(entidad):
    return instancias.get(entidad, {})

# Mostrar ontología y consultas
print("[Ontologías - Ingeniería del Conocimiento]")
print("Subclases de 'Transporte':", obtener_subclases('Transporte'))
print("Subclases de 'Ciudad':", obtener_subclases('Ciudad'))

print("\nInformación de entidades:")
for entidad in ['Camión', 'Avión', 'CDMX']:
    print(f"{entidad}: {obtener_info(entidad)}")
