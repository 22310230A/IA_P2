# Taxonomías: Categorías y Objetos
#
# Simulamos una estructura de categorías con objetos
# usando un sistema tipo árbol de clasificación jerárquica.

# Categorías y subcategorías
taxonomia = {
    'Vehículo': ['Terrestre', 'Aéreo'],
    'Terrestre': ['Camión', 'Auto', 'Motocicleta'],
    'Aéreo': ['Avión', 'Helicóptero'],
    'Ciudad': ['CDMX', 'Guadalajara', 'Querétaro']
}

# Objeto clasificado en una categoría
objetos = {
    'VolvoBus': 'Camión',
    'Mazda3': 'Auto',
    'Boeing737': 'Avión',
    'Harley': 'Motocicleta',
    'CDMX': 'Ciudad'
}

# Función para buscar categoría principal
def buscar_raiz(objeto):
    categoria = objetos.get(objeto)
    if not categoria:
        return "No encontrado"
    for padre, hijos in taxonomia.items():
        if categoria in hijos:
            return padre
    return "Categoría raíz desconocida"

# Mostrar clasificación
print("[Taxonomías - Categorías y Objetos]")

for obj in objetos:
    categoria = objetos[obj]
    raiz = buscar_raiz(obj)
    print(f"{obj} → {categoria} → {raiz}")
