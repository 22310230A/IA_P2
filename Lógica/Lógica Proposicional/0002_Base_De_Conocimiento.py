# Base de Conocimiento
#
# Creamos una base de conocimiento simple con hechos y reglas,
# y consultamos inferencias básicas a partir de ella.

# Base de conocimiento: lista de hechos
hechos = {
    'es_humano(alejandro)': True,
    'es_mortal(X)': 'es_humano(X)'
}

# Función para consultar hechos
def consultar(consulta):
    if consulta in hechos and hechos[consulta] == True:
        return True
    elif consulta in hechos and isinstance(hechos[consulta], str):
        regla = hechos[consulta]
        variable = consulta.split('(')[1].split(')')[0]
        regla_instanciada = regla.replace('X', variable)
        return consultar(regla_instanciada)
    else:
        return False

# Consultas
consultas = [
    'es_humano(alejandro)',
    'es_mortal(alejandro)',
    'es_humano(maria)'
]

print("[Base de Conocimiento]")
for c in consultas:
    resultado = consultar(c)
    print(f"Consulta: {c} => {'Verdadero' if resultado else 'Falso'}")
