"""
Ex1 - Demostracion de las formulas de diferencias finitas a partir de Taylor

La expansion de Taylor de f alrededor del punto x_i es:

  f(x_i + dx) = f_i + f'_i*dx + f''_i*dx^2/2 + f'''_i*dx^3/6 + ...   (A)
  f(x_i - dx) = f_i - f'_i*dx + f''_i*dx^2/2 - f'''_i*dx^3/6 + ...   (B)

De aqui se obtienen las tres aproximaciones para la primera derivada:

  - Diferencia hacia adelante (forward):  despejamos f'_i de (A)
        f'_i = (f_{i+1} - f_i) / dx  +  O(dx)       [orden 1]

  - Diferencia hacia atras (backward):    despejamos f'_i de (B)
        f'_i = (f_i - f_{i-1}) / dx  +  O(dx)        [orden 1]

  - Diferencia central (central):         (A) - (B), los terminos pares se cancelan
        f'_i = (f_{i+1} - f_{i-1}) / (2*dx)  +  O(dx^2)   [orden 2, mas precisa]

Y para la segunda derivada:
  - Diferencia central:                   (A) + (B), los terminos impares se cancelan
        f''_i = (f_{i+1} - 2*f_i + f_{i-1}) / dx^2  +  O(dx^2)   [orden 2]

---

Este script comprueba numericamente el error de cada formula
usando la funcion f(x) = sin(x), cuya derivada exacta es cos(x).
"""

import numpy as np
import matplotlib.pyplot as plt

# Funcion de prueba y su derivada exacta
def f(x):
    return np.sin(x)

def df_exacta(x):
    return np.cos(x)

# Punto donde evaluamos
x_i = 1.0   # radianes

# Probamos distintos valores de dx para ver como mejora el error
lista_dx    = [0.5, 0.1, 0.05, 0.01, 0.005, 0.001]
err_forward  = []
err_backward = []
err_central  = []

for dx in lista_dx:
    f_i      = f(x_i)
    f_mas    = f(x_i + dx)    # f_{i+1}
    f_menos  = f(x_i - dx)    # f_{i-1}
    deriv_exacta = df_exacta(x_i)

    # Las tres formulas
    forward  = (f_mas - f_i)         / dx
    backward = (f_i   - f_menos)     / dx
    central  = (f_mas - f_menos)     / (2 * dx)

    err_forward.append(abs(forward  - deriv_exacta))
    err_backward.append(abs(backward - deriv_exacta))
    err_central.append(abs(central  - deriv_exacta))

# Mostrar tabla de errores
print("dx        | Error forward | Error backward | Error central")
print("-" * 60)
for i in range(len(lista_dx)):
    print("{:.4f}    | {:.2e}     | {:.2e}      | {:.2e}".format(
        lista_dx[i], err_forward[i], err_backward[i], err_central[i]))

# Grafica: error en funcion de dx (escala log-log)
plt.figure()
plt.loglog(lista_dx, err_forward,  "o-",  label="Forward  (orden 1)")
plt.loglog(lista_dx, err_backward, "s-",  label="Backward (orden 1)")
plt.loglog(lista_dx, err_central,  "^-",  label="Central  (orden 2)")

# Lineas de referencia para ver la pendiente
dx_ref = np.array(lista_dx)
plt.loglog(dx_ref, dx_ref,     "k--", label="Pendiente orden 1")
plt.loglog(dx_ref, dx_ref**2,  "k:",  label="Pendiente orden 2")

plt.xlabel("dx")
plt.ylabel("Error absoluto")
plt.title("Ex1: Error de las diferencias finitas vs dx\nf(x) = sin(x),  f'(x) = cos(x)")
plt.legend()
plt.grid(True, which="both")
plt.savefig("ex1_resultado.png", dpi=150)
plt.show()

print("Grafica guardada como ex1_resultado.png")
print("Conclusion: la central tiene orden 2 (pendiente 2 en log-log)")
