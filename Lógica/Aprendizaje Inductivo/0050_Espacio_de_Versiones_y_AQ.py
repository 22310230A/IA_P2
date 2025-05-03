# Espacio de Versiones y Algoritmo AQ (simplificado)
#
# Se mantiene una hipótesis más general (G) y una más específica (S)
# que encierran el conjunto de hipótesis válidas.

# Atributos: [color, tamaño, forma]
positivos = [
    ['rojo', 'mediano', 'redonda'],
    ['rojo', 'grande', 'ovalada']
]

negativos = [
    ['verde', 'mediano', 'ovalada'],
    ['amarillo', 'grande', 'cuadrada']
]

# Inicializar hipótesis
S = positivos[0].copy()
G = ['?' for _ in S]

# Refinar S con ejemplos positivos
for ejemplo in positivos[1:]:
    for i in range(len(S)):
        if S[i] != ejemplo[i]:
            S[i] = '?'

# Refinar G con ejemplos negativos
for ejemplo in negativos:
    for i in range(len(G)):
        if S[i] != '?' and S[i] == ejemplo[i]:
            G[i] = '?'

print("[Espacio de Versiones - AQ simplificado]")
print("Hipótesis Específica (S):", S)
print("Hipótesis General (G):", G)
