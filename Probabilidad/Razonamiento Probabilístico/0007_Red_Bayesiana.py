# Red Bayesiana
#
# Una Red Bayesiana es una estructura que representa relaciones de probabilidad
# entre variables mediante un grafo dirigido acíclico (DAG).

# Usamos una versión reducida del grafo de ciudades:
#
# México → Querétaro → San Luis → Guadalajara

# Nodos:
# - México influye en Querétaro
# - Querétaro influye en San Luis
# - San Luis influye en Guadalajara

# Probabilidades condicionales (simuladas)
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

# Vamos a calcular la probabilidad de que el agente llegue a Guadalajara
# suponiendo que México = True (el agente salió de ahí)

# Paso 1: P(Querétaro | México = True)
P_Querétaro = P_Querétaro_dado_México[True]

# Paso 2: P(San Luis | Querétaro)
P_SanLuis = P_SanLuis_dado_Querétaro[True]

# Paso 3: P(Guadalajara | San Luis)
P_Guadalajara = P_Guadalajara_dado_SanLuis[True]

# Paso 4: Multiplicamos todas las probabilidades
P_final = P_México * P_Querétaro * P_SanLuis * P_Guadalajara

# Mostrar resultado
print("[Red Bayesiana]")
print(f"P(México) = {P_México}")
print(f"P(Querétaro | México) = {P_Querétaro}")
print(f"P(San Luis | Querétaro) = {P_SanLuis}")
print(f"P(Guadalajara | San Luis) = {P_Guadalajara}")
print(f"\nProbabilidad conjunta de llegar a Guadalajara: {P_final:.5f}")
