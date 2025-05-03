# Programación Lógica Inductiva: FOIL (simplificado)
#
# El objetivo es inducir una regla lógica que relacione hechos y predicados.
# Este ejemplo está muy simplificado para fines ilustrativos.

# Hechos positivos
positivos = [
    ('padre', 'juan', 'pedro'),
    ('padre', 'juan', 'maria')
]

# Hechos negativos
negativos = [
    ('padre', 'ana', 'pedro'),
    ('padre', 'juan', 'juan')
]

# Regla a inducir: Si X es padre de Y, entonces X es un padre
def inducir_regla(positivos, negativos):
    regla = []
    for hecho in positivos:
        if hecho not in negativos:
            sujeto = hecho[1]
            if sujeto not in regla:
                regla.append(sujeto)
    return regla

# Ejecutar
padres_inducidos = inducir_regla(positivos, negativos)

print("[Programación Lógica Inductiva - FOIL]")
print("Hechos positivos:", positivos)
print("Hechos negativos:", negativos)
print("Padres inducidos:", padres_inducidos)
