"""
Ex2 - Discretizacion de la ecuacion parabolica 1D

Ecuacion a discretizar:
    df/dt = alpha * d2f/dy2                              (5)

Con condiciones de contorno e inicial:
    f(t, y=0) = C1
    f(t, y=L) = C2
    f(t=0, y) = C3                                       (6)

------------------------------------------------------------
PASO 1: Discretizar el dominio
------------------------------------------------------------
Dividimos el tiempo t en pasos de dt:   t_k = k * dt,  k = 0, 1, ..., m
Dividimos el espacio y en pasos de dy:  y_j = j * dy,  j = 0, 1, ..., n

Usamos la notacion: f_j^k = f(t_k, y_j)

------------------------------------------------------------
PASO 2: Aproximar las derivadas con diferencias finitas
------------------------------------------------------------

Para df/dt usamos diferencia hacia adelante (orden 1):
    df/dt ≈ (f_j^{k+1} - f_j^k) / dt

Para d2f/dy2 usamos diferencia central (orden 2, mas precisa):
    d2f/dy2 ≈ (f_{j+1}^k - 2*f_j^k + f_{j-1}^k) / dy^2

------------------------------------------------------------
PASO 3: Sustituir en la ecuacion (5)
------------------------------------------------------------

    (f_j^{k+1} - f_j^k) / dt  =  alpha * (f_{j+1}^k - 2*f_j^k + f_{j-1}^k) / dy^2

Despejando f_j^{k+1} (el unico valor desconocido):

    f_j^{k+1} = f_j^k + alpha*dt/dy^2 * (f_{j+1}^k - 2*f_j^k + f_{j-1}^k)

Definiendo r = alpha*dt/dy^2 (numero de Courant):

    f_j^{k+1} = f_j^k + r * (f_{j+1}^k - 2*f_j^k + f_{j-1}^k)

    con  j = 1, 2, ..., n-1  (solo puntos interiores)

------------------------------------------------------------
PASO 4: Condiciones de contorno e inicial discretizadas (6)
------------------------------------------------------------

    f_0^k     = C1    para todo k  (frontera y=0, fija en el tiempo)
    f_n^k     = C2    para todo k  (frontera y=L, fija en el tiempo)
    f_j^0     = C3    para todo j  (condicion inicial en t=0)

------------------------------------------------------------
CONDICION DE ESTABILIDAD (Courant)
------------------------------------------------------------
El metodo explicito solo es estable si:
    r = alpha*dt/dy^2 <= 0.5

Si r > 0.5 el metodo diverge (la solucion crece sin control).

------------------------------------------------------------
Este script verifica la condicion de Courant para distintos dt
------------------------------------------------------------
"""

import numpy as np

alpha = 1.0   # difusividad
n     = 10    # intervalos en y
L     = 1.0   # longitud
dy    = L / n

print("Verificacion de la condicion de Courant: r = alpha*dt/dy^2 <= 0.5")
print("dy =", dy)
print()
print("dt         | r           | Estable?")
print("-" * 45)

lista_dt = [0.1, 0.05, 0.01, 0.005, 0.001]
for dt in lista_dt:
    r = alpha * dt / dy**2
    estable = "SI" if r <= 0.5 else "NO (inestable)"
    print("{:.4f}     | {:.4f}      | {}".format(dt, r, estable))

print()
print("La formula discretizada del Ex2 es:")
print("  f_j^(k+1) = f_j^k + r * (f_(j+1)^k - 2*f_j^k + f_(j-1)^k)")
print("Esta formula se implementa en ex3_parabolica.py")
