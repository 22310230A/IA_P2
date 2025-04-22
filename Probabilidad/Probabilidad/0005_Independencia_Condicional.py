# Independencia Condicional
#
# Dos variables son independientes condicionalmente si, dado un tercer valor conocido,
# conocer una no aporta información adicional sobre la otra.
#
# En nuestro grafo, se evaluará si "México" y "Guadalajara" son independientes
# al conocer un nodo intermedio como "San Luis" o "Querétaro".

# Grafo de ciudades (referencia visual):
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Guadalajara

# Supongamos que:
# - X = México
# - Y = Guadalajara
# - Z = San Luis

# Queremos saber si:
# P(Guadalajara | México, San Luis) = P(Guadalajara | San Luis)
# Si esto se cumple, entonces México ⊥ Guadalajara | San Luis

print("[Independencia Condicional]")

# Definimos distribuciones simuladas (ficticias) para ilustrar
P_GDL_dado_SLP = 0.8
P_GDL_dado_MEX_y_SLP = 0.8

print(f"P(Guadalajara | San Luis) = {P_GDL_dado_SLP}")
print(f"P(Guadalajara | México, San Luis) = {P_GDL_dado_MEX_y_SLP}")

if abs(P_GDL_dado_SLP - P_GDL_dado_MEX_y_SLP) < 0.01:
    print("Guadalajara y México son condicionalmente independientes dado San Luis.")
else:
    print("Hay dependencia condicional entre Guadalajara y México dado San Luis.")

# Otro caso: México y Guadalajara sin conocer San Luis
# Supongamos:
P_GDL_dado_MEX = 0.5
P_GDL = 0.7

print(f"\nP(Guadalajara) = {P_GDL}")
print(f"P(Guadalajara | México) = {P_GDL_dado_MEX}")

if abs(P_GDL - P_GDL_dado_MEX) < 0.01:
    print("Guadalajara y México son independientes sin condiciones.")
else:
    print("Guadalajara y México no son independientes sin condiciones.")
