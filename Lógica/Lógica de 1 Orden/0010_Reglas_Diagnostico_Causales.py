# Reglas de Diagnóstico y Causales
#
# Simulamos un sistema simple de diagnóstico basado en
# reglas causales entre síntomas y enfermedades.

# Base de conocimiento: reglas de causalidad
reglas_causales = {
    'fiebre': ['infeccion'],
    'tos': ['resfriado', 'infeccion'],
    'dolor_cabeza': ['migraña', 'resfriado'],
    'nausea': ['intoxicacion']
}

# Función de diagnóstico: dadas evidencias (síntomas), inferir posibles causas
def diagnosticar(sintomas_observados):
    posibles_causas = []
    for sintoma in sintomas_observados:
        causas = reglas_causales.get(sintoma, [])
        posibles_causas.extend(causas)
    return set(posibles_causas)

# Ejemplo de síntomas observados
sintomas = ['fiebre', 'tos']

# Realizar diagnóstico
causas_posibles = diagnosticar(sintomas)

# Mostrar resultados
print("[Reglas de Diagnóstico y Causales]")
print(f"Síntomas observados: {sintomas}")
print(f"Posibles causas diagnosticadas: {list(causas_posibles)}")
