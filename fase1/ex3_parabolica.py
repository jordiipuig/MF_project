import numpy as np
import matplotlib
matplotlib.use("Agg")   # quitar esta linea en PyCharm
import matplotlib.pyplot as plt

# Parametros fisicos
alpha = 1.0
L     = 1.0
C1    = 0.0    # valor en y=0
C2    = 1.0    # valor en y=L
C3    = 0.0    # valor inicial

# Parametros numericos
n  = 10        # numero de intervalos en y
m  = 1000      # numero de pasos de tiempo
T  = 1.0       # tiempo total

dy = L / n
dt = T / m
r  = alpha * dt / dy**2    # numero de Courant (debe ser <= 0.5)

print("r =", r)

# Coordenadas espaciales
y = np.linspace(0, L, n + 1)

# Condicion inicial
f = np.zeros(n + 1)
f[0] = C1
f[n] = C2

# Guardar perfiles en los pasos t10, t20, t30
f_t10 = np.zeros(n + 1)
f_t20 = np.zeros(n + 1)
f_t30 = np.zeros(n + 1)

# Bucle temporal
for k in range(m):
    if k == 10:
        f_t10 = f.copy()
    if k == 20:
        f_t20 = f.copy()
    if k == 30:
        f_t30 = f.copy()

    f_new = f.copy()
    for j in range(1, n):
        f_new[j] = f[j] + r * (f[j+1] - 2*f[j] + f[j-1])

    f_new[0] = C1
    f_new[n] = C2
    f = f_new

# Solucion analitica en estado estacionario: d2f/dy2 = 0 => f lineal en y
f_estacionario = np.zeros(n + 1)
for j in range(n + 1):
    f_estacionario[j] = C1 + (C2 - C1) * y[j] / L

plt.figure()
plt.plot(f_t10, y, label="t_10")
plt.plot(f_t20, y, label="t_20")
plt.plot(f_t30, y, label="t_30")
plt.plot(f_estacionario, y, "k--", label="Estacionario (analitico)")
plt.xlabel("f(t, y)")
plt.ylabel("y")
plt.title("Ex3: Ecuacion parabolica 1D")
plt.legend()
plt.grid(True)
plt.savefig("ex3_resultado.png", dpi=150)
plt.show()
