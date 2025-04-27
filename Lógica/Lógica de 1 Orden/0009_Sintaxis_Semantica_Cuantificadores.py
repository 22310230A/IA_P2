# Lógica de Primer Orden: Sintaxis y Semántica - Cuantificadores
#
# Simulamos el uso de cuantificadores universales (∀) y existenciales (∃)
# sobre un dominio de individuos.

# Dominio de individuos
individuos = ['alejandro', 'maria', 'juan']

# Propiedades
es_humano = {
    'alejandro': True,
    'maria': True,
    'juan': False
}

# Función para cuantificador universal (∀)
def para_todo(propiedad):
    return all(propiedad[individuo] for individuo in individuos)

# Función para cuantificador existencial (∃)
def existe(propiedad):
    return any(propiedad[individuo] for individuo in individuos)

# Evaluaciones
todos_humanos = para_todo(es_humano)
algun_humano = existe(es_humano)

# Mostrar resultados
print("[Sintaxis y Semántica: Cuantificadores]")
print(f"¿Todos los individuos son humanos? {'Sí' if todos_humanos else 'No'}")
print(f"¿Existe al menos un humano? {'Sí' if algun_humano else 'No'}")
