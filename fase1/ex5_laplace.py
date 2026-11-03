import numpy as np
import matplotlib
matplotlib.use("Agg")   # quitar esta linea en PyCharm
import matplotlib.pyplot as plt

# Parametros fisicos
K  = 2.0
Lx = 100.0
Ly = 100.0

# Parametros numericos
m      = 10    # intervalos en x
n      = 10    # intervalos en y
n_iter = 30    # numero de iteraciones

dx = Lx / m
dy = Ly / n

x = np.linspace(0, Lx, m + 1)
y = np.linspace(0, Ly, n + 1)

# Condicion inicial: promedio entre frontera inferior (0) y superior (K*Ly)
f_inicial = (0 + K * Ly) / 2.0

f = np.zeros((n + 1, m + 1))    # f[j][i]: j=indice y, i=indice x
for j in range(n + 1):
    for i in range(m + 1):
        f[j][i] = f_inicial

# Condiciones de contorno
for j in range(n + 1):
    f[j][0] = K * y[j]    # lado izquierdo
    f[j][m] = K * y[j]    # lado derecho
for i in range(m + 1):
    f[0][i] = 0.0          # lado inferior
    f[n][i] = K * Ly       # lado superior

f_it10 = np.zeros((n + 1, m + 1))
f_it20 = np.zeros((n + 1, m + 1))
f_it30 = np.zeros((n + 1, m + 1))

# Bucle de iteraciones de Jacobi:
# en cada iteracion f[j][i] = media de sus 4 vecinos (proviene de discretizar Laplace con dx=dy)
for it in range(1, n_iter + 1):
    f_new = f.copy()
    for j in range(1, n):
        for i in range(1, m):
            f_new[j][i] = 0.25 * (f[j+1][i] + f[j-1][i] + f[j][i+1] + f[j][i-1])

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

X, Y = np.meshgrid(x, y)

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

cp1 = axes[0].contourf(X, Y, f_it10, levels=20, cmap="viridis")
plt.colorbar(cp1, ax=axes[0])
axes[0].set_title("Iteracion 10")
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")

cp2 = axes[1].contourf(X, Y, f_it20, levels=20, cmap="viridis")
plt.colorbar(cp2, ax=axes[1])
axes[1].set_title("Iteracion 20")
axes[1].set_xlabel("x")

cp3 = axes[2].contourf(X, Y, f_it30, levels=20, cmap="viridis")
plt.colorbar(cp3, ax=axes[2])
axes[2].set_title("Iteracion 30")
axes[2].set_xlabel("x")

plt.suptitle("Ex5: Ecuacion de Laplace 2D - Metodo de Jacobi")
plt.tight_layout()
plt.savefig("ex5_resultado.png", dpi=150)
plt.show()

print("f[5][5] =", f_it30[5][5], "  (valor esperado:", K * y[n // 2], ")")
