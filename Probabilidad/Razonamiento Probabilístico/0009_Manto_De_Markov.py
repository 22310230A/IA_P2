# Manto de Markov (Markov Blanket)
#
# El manto de Markov de una variable X es el conjunto mínimo de nodos
# que, una vez conocidos, hacen que X sea condicionalmente independiente del resto.

# Grafo:
#
# México → Querétaro → San Luis → Guadalajara

# Queremos analizar el manto de Markov del nodo: San Luis

# En este ejemplo:
# - San Luis depende de Querétaro (padre)
# - Guadalajara depende de San Luis (hijo)

# El manto de Markov de San Luis es:
# - Querétaro (su padre)
# - Guadalajara (su hijo)

print("[Manto de Markov]")

# Variables en la red
nodos = ['México', 'Querétaro', 'San Luis', 'Guadalajara']

# Relaciones de dependencia (simplificadas)
dependencias = {
    'Querétaro': ['México'],
    'San Luis': ['Querétaro'],
    'Guadalajara': ['San Luis']
}

# Función para encontrar el manto de Markov de un nodo
def obtener_manto_de_markov(nodo, dependencias):
    manto = set()

    # Padres del nodo
    padres = [p for p in dependencias.get(nodo, [])]
    manto.update(padres)

    # Hijos del nodo
    hijos = [hijo for hijo, padres in dependencias.items() if nodo in padres]
    manto.update(hijos)

    # Padres de los hijos
    for hijo in hijos:
        manto.update(dependencias.get(hijo, []))

    return manto

nodo_objetivo = 'San Luis'
manto = obtener_manto_de_markov(nodo_objetivo, dependencias)

# Mostrar resultado
print(f"Manto de Markov de '{nodo_objetivo}': {sorted(manto)}")

# Verificación de independencia:
print(f"\nSan Luis es condicionalmente independiente del resto de nodos (como México y otros)")
print("si se conoce el valor de su manto: Querétaro, Guadalajara y padres de Guadalajara (si los hay).")
