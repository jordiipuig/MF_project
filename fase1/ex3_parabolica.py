"""
Ex3 - Metodo explicito para ecuacion parabolica 1D
Ecuacion: df/dt = alpha * d2f/dy2

Esquema FTCS (Forward in Time, Central in Space):
  f_new[j] = f[j] + r * (f[j+1] - 2*f[j] + f[j-1])
  donde r = alpha*dt/dy^2  (debe ser <= 0.5 para que sea estable)
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")   # permite guardar sin abrir ventana (quitar en PyCharm)
import matplotlib.pyplot as plt

# --- Parametros fisicos ---
alpha = 1.0    # difusividad (m^2/s)
L     = 1.0    # longitud del dominio en y (m)
C1    = 0.0    # condicion de contorno en y=0
C2    = 1.0    # condicion de contorno en y=L
C3    = 0.0    # condicion inicial en todo el dominio

# --- Parametros numericos ---
n  = 10        # numero de intervalos en y  (n+1 puntos)
m  = 1000      # numero de pasos de tiempo
T  = 1.0       # tiempo total de simulacion (s)

dy = L / n
dt = T / m
r  = alpha * dt / dy**2

print("dy =", dy, "  dt =", dt, "  r =", r)
if r <= 0.5:
    print("Condicion de estabilidad OK (r <= 0.5)")
else:
    print("ATENCION: r > 0.5, el metodo es inestable")

# --- Vectores de coordenadas ---
y = np.linspace(0, L, n + 1)   # y_0, y_1, ..., y_n

# --- Condicion inicial ---
f = np.zeros(n + 1)
for j in range(n + 1):
    f[j] = C3

# --- Condiciones de contorno ---
f[0] = C1     # frontera y=0
f[n] = C2     # frontera y=L

# --- Variables para guardar resultados en t10, t20, t30 ---
f_t10 = np.zeros(n + 1)
f_t20 = np.zeros(n + 1)
f_t30 = np.zeros(n + 1)

# --- Bucle temporal ---
for k in range(m):

    # Guardar el perfil en los pasos que nos interesan
    if k == 10:
        f_t10 = f.copy()
    if k == 20:
        f_t20 = f.copy()
    if k == 30:
        f_t30 = f.copy()

    # Calcular f en el instante siguiente (solo puntos interiores)
    f_new = f.copy()
    for j in range(1, n):
        f_new[j] = f[j] + r * (f[j+1] - 2*f[j] + f[j-1])

    # Mantener condiciones de contorno
    f_new[0] = C1
    f_new[n] = C2

    f = f_new

# --- Solucion analitica en estado estacionario ---
# Cuando t -> infinito, df/dt = 0 => d2f/dy2 = 0 => f = C1 + (C2-C1)*y/L
f_estacionario = np.zeros(n + 1)
for j in range(n + 1):
    f_estacionario[j] = C1 + (C2 - C1) * y[j] / L

# --- Grafica ---
plt.figure()

plt.plot(f_t10, y, label="t_10 (k=10)")
plt.plot(f_t20, y, label="t_20 (k=20)")
plt.plot(f_t30, y, label="t_30 (k=30)")
plt.plot(f_estacionario, y, "k--", label="Estado estacionario (analitico)")

plt.xlabel("f(t, y)")
plt.ylabel("y (m)")
plt.title("Ex3: Ecuacion parabolica 1D - Metodo explicito")
plt.legend()
plt.grid(True)
plt.savefig("ex3_resultado.png", dpi=150)
plt.show()

print("Grafica guardada como ex3_resultado.png")
