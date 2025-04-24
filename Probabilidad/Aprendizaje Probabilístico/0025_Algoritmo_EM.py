# Algoritmo EM (Expectation-Maximization)
#
# Se utiliza cuando hay variables ocultas y no se puede aplicar máxima verosimilitud directamente.
# En este ejemplo, intentamos estimar la media de dos grupos con datos mezclados.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  


# Generamos datos simulados: mezcla de dos gaussianas
np.random.seed(42)
n = 200
grupo1 = np.random.normal(5, 1, n//2)
grupo2 = np.random.normal(10, 1, n//2)
datos = np.hstack([grupo1, grupo2])
np.random.shuffle(datos)

# Inicialización aleatoria
mu1, mu2 = 4.0, 11.0
sigma1, sigma2 = 1.0, 1.0
pi1, pi2 = 0.5, 0.5

# Número de iteraciones
iteraciones = 15

# Algoritmo EM
for i in range(iteraciones):
    # E-step: calcular responsabilidades (prob. de pertenencia a cada grupo)
    r1 = pi1 * (1 / (np.sqrt(2 * np.pi) * sigma1)) * np.exp(- (datos - mu1) ** 2 / (2 * sigma1 ** 2))
    r2 = pi2 * (1 / (np.sqrt(2 * np.pi) * sigma2)) * np.exp(- (datos - mu2) ** 2 / (2 * sigma2 ** 2))
    total = r1 + r2
    r1 /= total
    r2 /= total

    # M-step: actualizar parámetros
    N1 = np.sum(r1)
    N2 = np.sum(r2)
    mu1 = np.sum(r1 * datos) / N1
    mu2 = np.sum(r2 * datos) / N2
    sigma1 = np.sqrt(np.sum(r1 * (datos - mu1) ** 2) / N1)
    sigma2 = np.sqrt(np.sum(r2 * (datos - mu2) ** 2) / N2)
    pi1 = N1 / n
    pi2 = N2 / n

    print(f"Iteración {i+1}: μ1={mu1:.2f}, μ2={mu2:.2f}, π1={pi1:.2f}, π2={pi2:.2f}")

# Visualización final
plt.hist(datos, bins=30, density=True, alpha=0.6, color='gray', label='Datos')
x = np.linspace(min(datos), max(datos), 100)
pdf1 = pi1 * (1 / (np.sqrt(2 * np.pi) * sigma1)) * np.exp(- (x - mu1)**2 / (2 * sigma1**2))
pdf2 = pi2 * (1 / (np.sqrt(2 * np.pi) * sigma2)) * np.exp(- (x - mu2)**2 / (2 * sigma2**2))
plt.plot(x, pdf1, label='Componente 1', color='blue')
plt.plot(x, pdf2, label='Componente 2', color='red')
plt.title("Algoritmo EM - Mezcla de Gaussianas")
plt.xlabel("Valor")
plt.ylabel("Densidad")
plt.legend()
plt.grid(True)
plt.show()
