# Mejor Hipótesis Actual
#
# Se parte de ejemplos positivos y se va generalizando la hipótesis
# hasta que sea coherente con todos los ejemplos vistos.

# Cada ejemplo tiene características como: [color, sabor, tamaño]

ejemplos = [
    ['rojo', 'dulce', 'mediano'],
    ['rojo', 'dulce', 'grande'],
    ['rojo', 'dulce', 'pequeño']
]

# Función que encuentra la hipótesis más general compatible
def mejor_hipotesis(ejemplos):
    hipotesis = ejemplos[0].copy()
    for ejemplo in ejemplos[1:]:
        for i in range(len(hipotesis)):
            if hipotesis[i] != ejemplo[i]:
                hipotesis[i] = '?'  # generaliza si hay diferencia
    return hipotesis

hipotesis_resultante = mejor_hipotesis(ejemplos)

print("[Mejor Hipótesis Actual]")
print("Ejemplos positivos:")
for ej in ejemplos:
    print("-", ej)
print("Hipótesis generalizada:", hipotesis_resultante)
