# Lógica por Defecto
#
# Simulamos razonamiento por defecto:
# asumimos que se puede viajar a una ciudad a menos que sepamos lo contrario.

# Conocimiento explícito: excepciones o bloqueos conocidos
rutas_bloqueadas = {
    ('san_luis', 'guadalajara')
}

# Función por defecto: se asume que se puede viajar si no está bloqueado
def puede_viajar(origen, destino):
    if (origen, destino) in rutas_bloqueadas:
        return False  # hay evidencia de que NO se puede
    return True  # por defecto se asume que sí se puede

# Consultas
consultas = [
    ('mexico', 'queretaro'),
    ('queretaro', 'san_luis'),
    ('san_luis', 'guadalajara'),
    ('guadalajara', 'cdmx')  # no se sabe nada, se asume que sí se puede
]

# Mostrar resultados
print("[Lógica por Defecto - Viajes]")
for origen, destino in consultas:
    resultado = puede_viajar(origen, destino)
    print(f"¿Se puede viajar de {origen} a {destino}? {'Sí (por defecto)' if resultado else 'No (bloqueado)'}")
