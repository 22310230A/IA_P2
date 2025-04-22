# Eliminación de Variables
#
# Es una técnica para calcular una probabilidad marginal
# al eliminar variables ocultas, evitando enumerar todas las combinaciones posibles.

# Red Bayesiana simplificada:
#
# México → Querétaro → San Luis → Guadalajara

# Queremos calcular: P(Guadalajara)
# Eliminaremos las variables México, Querétaro y San Luis una por una.

# Probabilidades (simuladas)
P_México = 0.3
P_Querétaro_dado_México = {True: 0.8, False: 0.2}
P_SanLuis_dado_Querétaro = {True: 0.9, False: 0.3}
P_Guadalajara_dado_SanLuis = {True: 0.95, False: 0.1}

# Valores posibles
valores = [True, False]

# Paso 1: Eliminamos México
# Calculamos P(Querétaro) = ∑ P(México) * P(Querétaro | México)
P_Querétaro = {
    True: P_México * P_Querétaro_dado_México[True] +
          (1 - P_México) * P_Querétaro_dado_México[False],
    False: P_México * (1 - P_Querétaro_dado_México[True]) +
           (1 - P_México) * (1 - P_Querétaro_dado_México[False])
}

# Paso 2: Eliminamos Querétaro → obtenemos P(San Luis)
P_SanLuis = {
    True: P_Querétaro[True] * P_SanLuis_dado_Querétaro[True] +
          P_Querétaro[False] * P_SanLuis_dado_Querétaro[False],
    False: P_Querétaro[True] * (1 - P_SanLuis_dado_Querétaro[True]) +
           P_Querétaro[False] * (1 - P_SanLuis_dado_Querétaro[False])
}

# Paso 3: Eliminamos San Luis → obtenemos P(Guadalajara)
P_Guadalajara = (
    P_SanLuis[True] * P_Guadalajara_dado_SanLuis[True] +
    P_SanLuis[False] * P_Guadalajara_dado_SanLuis[False]
)

# Mostrar resultado final
print("[Eliminación de Variables]")
print(f"P(Querétaro): {P_Querétaro}")
print(f"P(San Luis): {P_SanLuis}")
print(f"P(Guadalajara): {P_Guadalajara:.4f}")
