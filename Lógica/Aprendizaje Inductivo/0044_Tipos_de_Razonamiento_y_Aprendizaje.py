# Tipos de Razonamiento y Aprendizaje
#
# Este ejemplo muestra cómo se aplican diferentes formas de razonamiento
# y aprendizaje usando ejemplos concretos para clasificar frutas.

# Base de ejemplos
ejemplos = [
    {'color': 'rojo', 'forma': 'redonda', 'clase': 'manzana'},
    {'color': 'amarillo', 'forma': 'larga', 'clase': 'plátano'},
    {'color': 'naranja', 'forma': 'redonda', 'clase': 'naranja'},
    {'color': 'rojo', 'forma': 'larga', 'clase': 'chile'}
]

# Razonamiento inductivo: generaliza a partir de los ejemplos
def razonamiento_inductivo(ejemplos):
    reglas = []
    for ej in ejemplos:
        regla = f"Si es {ej['color']} y {ej['forma']} entonces es {ej['clase']}"
        reglas.append(regla)
    return reglas

# Razonamiento deductivo: aplica reglas conocidas
def razonamiento_deductivo(color, forma):
    if color == 'rojo' and forma == 'redonda':
        return 'manzana'
    elif color == 'amarillo' and forma == 'larga':
        return 'plátano'
    elif color == 'naranja' and forma == 'redonda':
        return 'naranja'
    elif color == 'rojo' and forma == 'larga':
        return 'chile'
    else:
        return 'desconocido'

# Mostrar reglas inductivas
print("[Razonamiento Inductivo]")
reglas = razonamiento_inductivo(ejemplos)
for r in reglas:
    print("-", r)

# Prueba con razonamiento deductivo
print("\n[Razonamiento Deductivo]")
prueba = {'color': 'rojo', 'forma': 'larga'}
resultado = razonamiento_deductivo(prueba['color'], prueba['forma'])
print(f"Entrada: {prueba}")
print(f"Clasificación: {resultado}")
