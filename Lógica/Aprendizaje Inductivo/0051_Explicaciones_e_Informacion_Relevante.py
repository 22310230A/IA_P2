# Explicaciones e Información Relevante
#
# Este código muestra cómo identificar qué atributos influyen más
# en la clasificación, para dar una explicación lógica.

# Base de datos: frutas con diferentes características
ejemplos = [
    {'color': 'rojo', 'forma': 'redonda', 'dulce': True, 'es_fruta': True},
    {'color': 'verde', 'forma': 'ovalada', 'dulce': False, 'es_fruta': False},
    {'color': 'amarillo', 'forma': 'redonda', 'dulce': True, 'es_fruta': True},
    {'color': 'morado', 'forma': 'alargada', 'dulce': False, 'es_fruta': False},
]

# Función que da una "explicación" con base en patrones
def explicar(ejemplos):
    atributos_relevantes = []
    claves = list(ejemplos[0].keys())
    claves.remove('es_fruta')

    for clave in claves:
        valores_verdaderos = set(e[clave] for e in ejemplos if e['es_fruta'])
        valores_falsos = set(e[clave] for e in ejemplos if not e['es_fruta'])
        if not valores_verdaderos.isdisjoint(valores_falsos):
            continue
        atributos_relevantes.append(clave)
    
    return atributos_relevantes

relevantes = explicar(ejemplos)

print("[Explicaciones e Información Relevante]")
print("Atributos que ayudan a clasificar correctamente:", relevantes)
