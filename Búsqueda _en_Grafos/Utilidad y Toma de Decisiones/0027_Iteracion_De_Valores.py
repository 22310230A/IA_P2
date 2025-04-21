# Iteración de Valores
# Grafo nuevo (como MDP):
#
#           CDMX
#        /       \
#    León         Morelia
#     |               |
#  Aguascalientes   Tepatitlán
#         \       /
#         Guadalajara
#
# Objetivo: llegar a Guadalajara (GDL)
# Recompensas negativas por el camino, positivas al llegar

# Estados (ciudades)
estados = ['CDMX', 'León', 'Morelia', 'Aguascalientes', 'Tepatitlán', 'Guadalajara']

# Transiciones: estado → [(siguiente_estado, recompensa)]
transiciones = {
    'CDMX': [('León', -2), ('Morelia', -3)],
    'León': [('Aguascalientes', -4)],
    'Morelia': [('Tepatitlán', -4)],
    'Aguascalientes': [('Guadalajara', 10)],
    'Tepatitlán': [('Guadalajara', 10)],
    'Guadalajara': []
}

# Inicialización de valores
valores = {estado: 0 for estado in estados}

# Parámetros
gamma = 0.9  # Factor de descuento
umbral = 0.01  # Criterio de convergencia

def iteracion_de_valores():
    global valores
    cambio = float('inf')

    while cambio > umbral:
        nuevo_valores = valores.copy()
        cambio = 0

        for estado in estados:
            if not transiciones[estado]:
                continue  # Estado terminal (GDL)

            max_valor = float('-inf')
            for siguiente, recompensa in transiciones[estado]:
                valor_estimado = recompensa + gamma * valores[siguiente]
                max_valor = max(max_valor, valor_estimado)

            nuevo_valores[estado] = max_valor
            cambio = max(cambio, abs(valores[estado] - max_valor))

        valores = nuevo_valores

# Ejecutar
iteracion_de_valores()

# Mostrar resultados
print("[Iteración de Valores] Valor estimado por ciudad:")
for estado in estados:
    print(f"{estado}: {valores[estado]:.2f}")
