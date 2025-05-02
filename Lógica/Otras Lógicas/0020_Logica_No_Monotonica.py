# Lógica No Monotónica
#
# Simulamos cómo una conclusión deja de ser válida al agregar nueva información.

# Base de conocimiento inicial con tuplas reales como claves
hechos = {
    ('mexico', 'queretaro'): True,
    ('queretaro', 'san_luis'): True,
    ('san_luis', 'guadalajara'): True
}

# Función para inferencia: ¿puede llegar de origen a destino?
def puede_llegar(origen, destino, visitados=None):
    if visitados is None:
        visitados = set()
    if origen == destino:
        return True
    visitados.add(origen)
    for (a, b), valido in hechos.items():
        if valido and a == origen and b not in visitados:
            if puede_llegar(b, destino, visitados):
                return True
    return False

# Primera evaluación
resultado1 = puede_llegar('mexico', 'guadalajara')

# Se bloquea una ruta (nueva información)
hechos[('san_luis', 'guadalajara')] = False

# Segunda evaluación
resultado2 = puede_llegar('mexico', 'guadalajara')

# Mostrar resultados
print("[Lógica No Monotónica - Viajes]")
print(f"Inicialmente, ¿puede llegar de México a Guadalajara?: {'Sí' if resultado1 else 'No'}")
print("Después de bloquear la ruta San Luis → Guadalajara:")
print(f"¿Aún puede llegar?: {'Sí' if resultado2 else 'No'}")
