# Regla de Bayes
#
# La regla de Bayes permite invertir la probabilidad condicional.
# A partir de P(evidencia | causa) y P(causa), obtenemos P(causa | evidencia).
#
# Se usa mucho para actualizar creencias luego de observar algo.

# Ejemplo con nuestro grafo:
#
# Supongamos que recibimos la señal "zona industrial",
# y queremos saber la probabilidad de que el agente esté en Querétaro,
# usando la Regla de Bayes.

# Valores conocidos:
P_Querétaro = 0.1                        # Probabilidad a priori de estar en Querétaro
P_zona_industrial_dado_Querétaro = 0.9  # Probabilidad de observar zona industrial si estás en Querétaro

# También necesitamos P(zona industrial) como normalizador:
# Esto se calcula usando todas las ciudades (como en ejemplos anteriores)

P_prior = {
    'México': 0.3,
    'Querétaro': 0.1,
    'Puebla': 0.2,
    'San Luis': 0.1,
    'Veracruz': 0.2,
    'Guadalajara': 0.1
}

P_obs_dado_ciudad = {
    'México': 0.2,
    'Querétaro': 0.9,
    'Puebla': 0.1,
    'San Luis': 0.8,
    'Veracruz': 0.2,
    'Guadalajara': 0.1
}

# Paso 1: Calcular P(zona industrial) usando la ley de la probabilidad total
P_evidencia = sum(
    P_obs_dado_ciudad[c] * P_prior[c]
    for c in P_prior
)

# Paso 2: Aplicar la Regla de Bayes
P_Querétaro_dado_zona_industrial = (P_zona_industrial_dado_Querétaro * P_Querétaro) / P_evidencia

# Mostrar resultados
print("[Regla de Bayes]")
print(f"P(zona industrial) = {P_evidencia:.4f}")
print(f"P(Querétaro | zona industrial) = {P_Querétaro_dado_zona_industrial:.4f}")
