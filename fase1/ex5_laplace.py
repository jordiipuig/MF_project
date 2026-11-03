"""
Ex4 + Ex5 - Metodo iterativo (Jacobi) para ecuacion de Laplace 2D
Ecuacion: d2f/dx2 + d2f/dy2 = 0

Discretizacion (diferencias centrales, con Dx=Dy):
  f[j][i] = 0.25 * (f[j+1][i] + f[j-1][i] + f[j][i+1] + f[j][i-1])

Condiciones de contorno:
  f(x=0,  y) = K*y      (lado izquierdo)
  f(x=Lx, y) = K*y      (lado derecho)
  f(x,  y=0) = 0        (lado inferior)
  f(x, y=Ly) = K*Ly     (lado superior)
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")   # permite guardar sin abrir ventana (quitar en PyCharm)
import matplotlib.pyplot as plt

# --- Parametros fisicos ---
K  = 2.0     # constante (unidades internacionales)
Lx = 100.0   # longitud en x (m)
Ly = 100.0   # longitud en y (m)

# --- Parametros numericos ---
m      = 10   # intervalos en x  (m+1 puntos)
n      = 10   # intervalos en y  (n+1 puntos)
n_iter = 30   # numero de iteraciones

dx = Lx / m
dy = Ly / n

# --- Vectores de coordenadas ---
x = np.linspace(0, Lx, m + 1)   # x_0, x_1, ..., x_m
y = np.linspace(0, Ly, n + 1)   # y_0, y_1, ..., y_n

# --- Condicion inicial: promedio entre fronteras inferior (0) y superior (K*Ly) ---
f_inicial = (0 + K * Ly) / 2.0

f = np.zeros((n + 1, m + 1))   # f[j][i] donde j es indice en y, i en x
for j in range(n + 1):
    for i in range(m + 1):
        f[j][i] = f_inicial

# --- Aplicar condiciones de contorno (se mantienen fijas en todas las iteraciones) ---
for j in range(n + 1):
    f[j][0]  = K * y[j]    # lado izquierdo x=0
    f[j][m]  = K * y[j]    # lado derecho x=Lx

for i in range(m + 1):
    f[0][i]  = 0.0         # lado inferior y=0
    f[n][i]  = K * Ly      # lado superior y=Ly

# --- Variables para guardar resultados en iteracion 10, 20, 30 ---
f_it10 = np.zeros((n + 1, m + 1))
f_it20 = np.zeros((n + 1, m + 1))
f_it30 = np.zeros((n + 1, m + 1))

# --- Bucle de iteraciones (metodo de Jacobi) ---
for it in range(1, n_iter + 1):

    f_new = f.copy()

    # Actualizar solo los puntos interiores
    for j in range(1, n):
        for i in range(1, m):
            f_new[j][i] = 0.25 * (f[j+1][i] + f[j-1][i] + f[j][i+1] + f[j][i-1])

    # Mantener condiciones de contorno
    for j in range(n + 1):
        f_new[j][0] = K * y[j]
        f_new[j][m] = K * y[j]
    for i in range(m + 1):
        f_new[0][i] = 0.0
        f_new[n][i] = K * Ly

    f = f_new

    if it == 10:
        f_it10 = f.copy()
    if it == 20:
        f_it20 = f.copy()
    if it == 30:
        f_it30 = f.copy()

# --- Grafica: contornos en iteracion 10, 20 y 30 ---
X, Y = np.meshgrid(x, y)

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

cp1 = axes[0].contourf(X, Y, f_it10, levels=20, cmap="viridis")
plt.colorbar(cp1, ax=axes[0])
axes[0].set_title("Iteracion 10")
axes[0].set_xlabel("x (m)")
axes[0].set_ylabel("y (m)")

cp2 = axes[1].contourf(X, Y, f_it20, levels=20, cmap="viridis")
plt.colorbar(cp2, ax=axes[1])
axes[1].set_title("Iteracion 20")
axes[1].set_xlabel("x (m)")

cp3 = axes[2].contourf(X, Y, f_it30, levels=20, cmap="viridis")
plt.colorbar(cp3, ax=axes[2])
axes[2].set_title("Iteracion 30")
axes[2].set_xlabel("x (m)")

plt.suptitle("Ex5: Ecuacion de Laplace 2D - Metodo iterativo de Jacobi")
plt.tight_layout()
plt.savefig("ex5_resultado.png", dpi=150)
plt.show()

# --- Interpretacion ---
print("Valor en el centro del dominio despues de 30 iteraciones:")
print("  f[5][5] =", f_it30[5][5])
print("Valor analitico esperado (K*y en el centro):", K * y[n // 2])
print("Grafica guardada como ex5_resultado.png")
