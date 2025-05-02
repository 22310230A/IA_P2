# Eventos y Objetos Mentales: Creencias
#
# Simulamos un sistema donde los agentes tienen creencias sobre el mundo
# y esas creencias pueden cambiar con nueva información.

# Base de creencias del agente
creencias = {
    'alejandro': {'llueve_en(queretaro)': True, 'puede_viajar(cdmx, queretaro)': True},
    'julio': {'llueve_en(queretaro)': False, 'puede_viajar(cdmx, queretaro)': False}
}

# Función para consultar si un agente cree algo
def cree(agente, proposicion):
    return creencias.get(agente, {}).get(proposicion, None)

# Función para actualizar una creencia
def actualizar_creencia(agente, proposicion, valor):
    if agente not in creencias:
        creencias[agente] = {}
    creencias[agente][proposicion] = valor

# Mostrar creencias actuales
print("[Eventos y Objetos Mentales - Creencias]\n")
for persona in creencias:
    print(f"Creencias de {persona.capitalize()}:")
    for prop, val in creencias[persona].items():
        print(f"  Cree que {prop.replace('_', ' ')}: {'Sí' if val else 'No'}")
    print()

# Nueva información llega a Alejandro
print("→ Nueva información para Alejandro: ya no llueve en Querétaro\n")
actualizar_creencia('alejandro', 'llueve_en(queretaro)', False)

# Verificar actualización
print("Creencias actualizadas de Alejandro:")
for prop, val in creencias['alejandro'].items():
    print(f"  Cree que {prop.replace('_', ' ')}: {'Sí' if val else 'No'}")
