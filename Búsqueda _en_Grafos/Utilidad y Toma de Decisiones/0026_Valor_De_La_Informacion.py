# Valor de la Información:
# El agente debe decidir si llevar sombrilla.
# Puede pagar por saber con certeza si lloverá.
#
# ¿Vale la pena pagar por esa información?

# Probabilidades del clima
prob_clima = {
    'lluvia': 0.3,
    'soleado': 0.7
}

# Utilidades de cada decisión dependiendo del clima
utilidad = {
    'llevar': {
        'lluvia': 90,
        'soleado': 60
    },
    'no_llevar': {
        'lluvia': 10,
        'soleado': 100
    }
}

def utilidad_esperada_sin_info():
    decisiones = ['llevar', 'no_llevar']
    mejores_utilidades = {}

    for decision in decisiones:
        total = 0
        for estado, prob in prob_clima.items():
            total += prob * utilidad[decision][estado]
        mejores_utilidades[decision] = total

    return max(mejores_utilidades.values())

def utilidad_esperada_con_info():
    return (
        prob_clima['lluvia'] * max(utilidad['llevar']['lluvia'], utilidad['no_llevar']['lluvia']) +
        prob_clima['soleado'] * max(utilidad['llevar']['soleado'], utilidad['no_llevar']['soleado'])
    )

# Costo de la información
costo_info = 5

# Cálculos
sin_info = utilidad_esperada_sin_info()
con_info = utilidad_esperada_con_info()
valor_info = con_info - sin_info

print(f"Utilidad esperada sin información: {sin_info:.2f}")
print(f"Utilidad esperada con información perfecta: {con_info:.2f}")
print(f"Valor de la información: {valor_info:.2f}")

if valor_info > costo_info:
    print("✅ Vale la pena pagar por la información.")
else:
    print("❌ No vale la pena pagar por la información.")
