# Inferencia por Enumeración
#
# Calculamos la probabilidad de que el agente esté en San Luis
# dado que observamos que llegó a Guadalajara.

# Grafo usado:
#
# México → Querétaro → San Luis → Guadalajara

# Probabilidades simuladas (como en los ejemplos anteriores)
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

# Enumeraremos todas las combinaciones posibles de:
# México, Querétaro, San Luis, Guadalajara
# Solo nos interesan aquellas donde Guadalajara=True
# y queremos calcular: P(San Luis=True | Guadalajara=True)

# Posibles valores booleanos
valores = [True, False]

# Acumuladores para numerador y denominador
num = 0
den = 0

for mex in valores:
    P_m = P_México if mex else (1 - P_México)
    P_q = P_Querétaro_dado_México[mex]

    for quer in valores:
        P_qr = P_q if quer else (1 - P_q)
        P_s = P_SanLuis_dado_Querétaro[quer]

        for sl in valores:
            P_sl = P_s if sl else (1 - P_s)
            P_g = P_Guadalajara_dado_SanLuis[sl]

            # Solo sumamos si Guadalajara=True (evidencia)
            if True:
                conjunto = P_m * P_qr * P_sl * P_g
                den += conjunto
                if sl:  # San Luis = True
                    num += conjunto

# Resultado final
P_SL_dado_GDL = num / den

print("[Inferencia por Enumeración]")
print(f"P(San Luis = True | Guadalajara = True) = {P_SL_dado_GDL:.4f}")
