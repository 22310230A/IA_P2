# Backtracking
#
# Implementamos un ejemplo clásico de backtracking:
# encontrar una solución a un problema probando opciones y retrocediendo si es necesario.

# Ejemplo: resolver una suma simple con restricciones
# Buscar tres números del 1 al 9 que sumen exactamente 15

def backtracking(solucion, suma_actual, objetivo, profundidad):
    if profundidad == 3:
        return suma_actual == objetivo, solucion
    
    for numero in range(1, 10):
        if numero not in solucion:  # Evitar repetir números
            nueva_solucion = solucion + [numero]
            nuevo_suma = suma_actual + numero
            exito, resultado = backtracking(nueva_solucion, nuevo_suma, objetivo, profundidad + 1)
            if exito:
                return True, resultado
    
    return False, []

# Ejecutar
objetivo = 15
exito, solucion = backtracking([], 0, objetivo, 0)

# Mostrar resultados
print("[Backtracking]")
if exito:
    print(f"Solución encontrada: {solucion}")
else:
    print("No se encontró solución.")
