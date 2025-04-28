# Resolución: Skolem
#
# Simulamos el proceso de skolemización: eliminar cuantificadores existenciales
# en una fórmula lógica reemplazándolos con funciones o constantes de Skolem.

# Fórmula de ejemplo (informalmente):
# ∀x ∃y viaja(x, y)
#
# Skolemización:
# Reemplazamos ∃y por una función de Skolem f(x), obteniendo:
# viaja(x, f(x))

# Simulamos un dominio
dominio = ['mexico', 'queretaro', 'san_luis']

# Definimos la función de Skolem
def funcion_skolem(x):
    # Definimos un destino fijo para cada origen (sólo a modo de ejemplo)
    destinos = {
        'mexico': 'queretaro',
        'queretaro': 'san_luis',
        'san_luis': 'guadalajara'
    }
    return destinos.get(x, 'desconocido')

# Aplicar la skolemización
def aplicar_skolem(dominio):
    relaciones = []
    for origen in dominio:
        destino = funcion_skolem(origen)
        relaciones.append(f"viaja({origen}, {destino})")
    return relaciones

# Ejecutar
relaciones_skolemizadas = aplicar_skolem(dominio)

# Mostrar resultados
print("[Resolución: Skolem]")
print("Relaciones skolemizadas:")
for relacion in relaciones_skolemizadas:
    print(f"  {relacion}")
