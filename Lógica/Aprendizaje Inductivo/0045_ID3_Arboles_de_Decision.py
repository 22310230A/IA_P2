# Árbol de Decisión con ID3 (simulado de forma sencilla)
#
# Este código muestra una forma muy básica de construir y usar un árbol de decisión.
# No usamos librerías externas, solo una estructura simple para entender el concepto.

# Datos de ejemplo (clima y decisión de salir)
datos = [
    {'clima': 'soleado', 'humedad': 'alta', 'salir': 'no'},
    {'clima': 'soleado', 'humedad': 'normal', 'salir': 'sí'},
    {'clima': 'lluvioso', 'humedad': 'alta', 'salir': 'sí'},
    {'clima': 'nublado', 'humedad': 'alta', 'salir': 'sí'},
    {'clima': 'nublado', 'humedad': 'normal', 'salir': 'sí'},
    {'clima': 'lluvioso', 'humedad': 'normal', 'salir': 'sí'},
    {'clima': 'soleado', 'humedad': 'alta', 'salir': 'no'}
]

# Árbol de decisión simulado como diccionario
arbol = {
    'clima': {
        'soleado': {
            'humedad': {
                'alta': 'no',
                'normal': 'sí'
            }
        },
        'lluvioso': 'sí',
        'nublado': 'sí'
    }
}

# Función de predicción usando el árbol
def predecir(entrada, arbol):
    if isinstance(arbol, dict):
        atributo = next(iter(arbol))
        valor = entrada.get(atributo)
        sub_arbol = arbol[atributo].get(valor)
        return predecir(entrada, sub_arbol)
    else:
        return arbol

# Prueba de predicción
entrada_prueba = {'clima': 'soleado', 'humedad': 'alta'}
resultado = predecir(entrada_prueba, arbol)

print("[Árbol de Decisión ID3]")
print("Entrada:", entrada_prueba)
print("¿Salir?:", resultado)
