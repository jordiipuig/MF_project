"""
Ex4 - Discretizacion de la ecuacion de Laplace 2D

Ecuacion a discretizar:
    d2f/dx2 + d2f/dy2 = 0                               (7)

Con condiciones de contorno Dirichlet:
    f(x=0,  y) = K*y
    f(x=Lx, y) = K*y
    f(x,  y=0) = 0
    f(x, y=Ly) = K*Ly                                   (8)

------------------------------------------------------------
PASO 1: Discretizar el dominio 2D
------------------------------------------------------------
Dividimos x en m intervalos: x_i = i*dx,  i = 0, 1, ..., m   (dx = Lx/m)
Dividimos y en n intervalos: y_j = j*dy,  j = 0, 1, ..., n   (dy = Ly/n)

Notacion: f_{i,j} = f(x_i, y_j)

------------------------------------------------------------
PASO 2: Aproximar las derivadas con diferencias centrales (orden 2)
------------------------------------------------------------

    d2f/dx2 ≈ (f_{i+1,j} - 2*f_{i,j} + f_{i-1,j}) / dx^2

    d2f/dy2 ≈ (f_{i,j+1} - 2*f_{i,j} + f_{i,j-1}) / dy^2

------------------------------------------------------------
PASO 3: Sustituir en la ecuacion (7)
------------------------------------------------------------

    (f_{i+1,j} - 2*f_{i,j} + f_{i-1,j}) / dx^2
  + (f_{i,j+1} - 2*f_{i,j} + f_{i,j-1}) / dy^2  = 0

Si usamos malla cuadrada (dx = dy):

    f_{i+1,j} - 2*f_{i,j} + f_{i-1,j}
  + f_{i,j+1} - 2*f_{i,j} + f_{i,j-1}  = 0

    f_{i+1,j} + f_{i-1,j} + f_{i,j+1} + f_{i,j-1} - 4*f_{i,j} = 0

Despejando f_{i,j}:

    f_{i,j} = 0.25 * (f_{i+1,j} + f_{i-1,j} + f_{i,j+1} + f_{i,j-1})

    con  i = 1, ..., m-1  y  j = 1, ..., n-1  (solo puntos interiores)

------------------------------------------------------------
INTERPRETACION
------------------------------------------------------------
El valor en cada punto interior es el PROMEDIO de sus 4 vecinos.
Como no conocemos ningun valor interior, iteramos:
  - Hacemos una suposicion inicial (guess)
  - Aplicamos la formula repetidamente hasta que converja
  -> Esto es el metodo de Jacobi (implementado en ex5_laplace.py)

------------------------------------------------------------
PASO 4: Condiciones de contorno discretizadas (8)
------------------------------------------------------------

    f_{0,j}  = K * y_j    para todo j  (lado izquierdo x=0)
    f_{m,j}  = K * y_j    para todo j  (lado derecho  x=Lx)
    f_{i,0}  = 0          para todo i  (lado inferior y=0)
    f_{i,n}  = K * Ly     para todo i  (lado superior y=Ly)

------------------------------------------------------------
No hay codigo de simulacion aqui, solo la deduccion.
La implementacion esta en ex5_laplace.py
------------------------------------------------------------
"""

print("Este archivo contiene la deduccion del Ex4.")
print()
print("Formula discretizada de Laplace 2D (con dx = dy):")
print("  f[i,j] = 0.25 * (f[i+1,j] + f[i-1,j] + f[i,j+1] + f[i,j-1])")
print()
print("Condiciones de contorno discretizadas:")
print("  f[0,j]  = K * y[j]   (izquierda)")
print("  f[m,j]  = K * y[j]   (derecha)")
print("  f[i,0]  = 0           (abajo)")
print("  f[i,n]  = K * Ly      (arriba)")
print()
print("La implementacion del metodo iterativo de Jacobi esta en ex5_laplace.py")
