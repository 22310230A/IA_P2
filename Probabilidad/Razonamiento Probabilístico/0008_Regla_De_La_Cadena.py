# Regla de la Cadena
#
# La regla de la cadena permite descomponer la probabilidad conjunta de varios eventos
# en un producto de probabilidades condicionales.

# Por ejemplo:
# P(A, B, C) = P(A) * P(B | A) * P(C | A, B)

# Usamos el mismo grafo lineal:
# México → Querétaro → San Luis → Guadalajara

# Variables:
# A = México
# B = Querétaro
# C = San Luis
# D = Guadalajara

# Probabilidades (simuladas)
P_México = 0.3
P_Querétaro_dado_México = {
    True: 0.8,
    False: 0.2
}
P_SanLuis_dado_Querétaro = {
    True: 0.9,
    False: 0.3
}
P_Guadalajara_dado_SanLuis = {
    True: 0.95,
    False: 0.1
}

# Usamos la Regla de la Cadena para calcular:
# P(México, Querétaro, San Luis, Guadalajara)

# Paso a paso:
P_Querétaro = P_Querétaro_dado_México[True]
P_SanLuis = P_SanLuis_dado_Querétaro[True]
P_Guadalajara = P_Guadalajara_dado_SanLuis[True]

# Aplicar regla de la cadena
P_total = P_México * P_Querétaro * P_SanLuis * P_Guadalajara

# Mostrar cálculo
print("[Regla de la Cadena]")
print(f"P(México) = {P_México}")
print(f"P(Querétaro | México) = {P_Querétaro}")
print(f"P(San Luis | Querétaro) = {P_SanLuis}")
print(f"P(Guadalajara | San Luis) = {P_Guadalajara}")
print(f"\nProbabilidad conjunta: P(M, Q, SL, GDL) = {P_total:.5f}")
