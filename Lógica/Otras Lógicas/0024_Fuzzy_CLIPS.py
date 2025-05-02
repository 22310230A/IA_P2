# Lógica Difusa: Fuzzy CLIPS (simulado en Python)
#
# Simulamos reglas tipo Fuzzy CLIPS con condiciones difusas y
# grados de verdad para inferencias múltiples.

# Base difusa: reglas tipo Fuzzy CLIPS
def evaluar_temperatura(temp):
    if temp <= 20:
        return 'frio', 1
    elif 20 < temp < 30:
        return 'templado', (30 - temp) / 10
    else:
        return 'calor', 1

# Reglas de tipo Fuzzy CLIPS
def fuzzy_clips(temp):
    estado, grado = evaluar_temperatura(temp)
    
    if estado == 'frio':
        respuesta = 'ventilador apagado'
    elif estado == 'templado':
        respuesta = 'ventilador medio'
    else:
        respuesta = 'ventilador fuerte'
    
    return estado, grado, respuesta

# Ejemplo de entrada
temperaturas = [18, 25, 35]

print("[Fuzzy CLIPS - Simulación en Python]")
for t in temperaturas:
    estado, grado, accion = fuzzy_clips(t)
    print(f"Temperatura: {t}°C")
    print(f"  Estado lingüístico: {estado}")
    print(f"  Grado de verdad: {grado:.2f}")
    print(f"  Acción recomendada: {accion}\n")
