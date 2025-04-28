# Lógicas de Orden Superior
#
# Simulamos el concepto de lógica de orden superior:
# funciones que toman otras funciones como argumentos.

# Función que representa una propiedad: ser mayor que 5
def mayor_que_5(x):
    return x > 5

# Función de orden superior que recibe una propiedad
def cumple_propiedad(dominio, propiedad):
    return [elemento for elemento in dominio if propiedad(elemento)]

# Dominio de ejemplo
dominio = [2, 4, 6, 8, 10]

# Aplicar función de orden superior
resultado = cumple_propiedad(dominio, mayor_que_5)

# Mostrar resultados
print("[Lógicas de Orden Superior]")
print(f"Dominio: {dominio}")
print("Elementos que cumplen 'mayor que 5':", resultado)
