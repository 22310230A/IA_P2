# Inferencia Lógica Proposicional
#
# Simulamos inferencias básicas usando modus ponens:
# si sabemos que "p" es verdadero y "p implica q", podemos deducir "q".

# Base de conocimiento
hechos = {
    'p': True,
    'p⇒q': True,  # p implica q
    'q⇒r': True   # q implica r
}

# Función de inferencia basada en modus ponens
def inferir(hechos):
    nuevos_hechos = hechos.copy()
    cambio = True

    while cambio:
        cambio = False
        for clave in list(nuevos_hechos.keys()):
            if '⇒' in clave:
                antecedente, consecuente = clave.split('⇒')
                if nuevos_hechos.get(antecedente, False) and not nuevos_hechos.get(consecuente, False):
                    nuevos_hechos[consecuente] = True
                    cambio = True
    return nuevos_hechos

# Ejecutar inferencia
hechos_inferidos = inferir(hechos)

# Mostrar resultados
print("[Inferencia Lógica Proposicional]")
for hecho, valor in hechos_inferidos.items():
    print(f"{hecho}: {'Verdadero' if valor else 'Falso'}")
