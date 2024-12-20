""" Comparaison de méthodes de résolution des équations différentielles ordinaires """

import numpy as np
import matplotlib.pyplot as plt

# Définition de l'EDO
def f(t, y):
    return -2 * y

# Solution analytique
def solution_analytique(t):
    return np.exp(-2 * t)

# Méthode d'Euler explicite
def euler_explicit(f, y0, t0, tf, h):
    t = np.arange(t0, tf + h, h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i - 1] + h * f(t[i - 1], y[i - 1])
    return t, y

# Méthode d'Euler implicite
def euler_implicit(f, y0, t0, tf, h):
    t = np.arange(t0, tf + h, h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        # Résolution implicite pour y_{i+1}: y_{i+1} = y_i / (1 + 2h)
        y[i] = y[i - 1] / (1 + 2 * h)
    return t, y

# Méthode de Runge-Kutta d'ordre 4
def runge_kutta_4(f, y0, t0, tf, h):
    t = np.arange(t0, tf + h, h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        k1 = h * f(t[i - 1], y[i - 1])
        k2 = h * f(t[i - 1] + h / 2, y[i - 1] + k1 / 2)
        k3 = h * f(t[i - 1] + h / 2, y[i - 1] + k2 / 2)
        k4 = h * f(t[i - 1] + h, y[i - 1] + k3)
        y[i] = y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return t, y

# Paramètres de simulation
y0 = 1         # Condition initiale
t0, tf = 0, 5  # Intervalle de temps
h = 0.3        # Pas de temps

# Résolution avec différentes méthodes
t_euler_exp, y_euler_exp = euler_explicit(f, y0, t0, tf, h)
t_euler_imp, y_euler_imp = euler_implicit(f, y0, t0, tf, h)
t_rk4, y_rk4 = runge_kutta_4(f, y0, t0, tf, h)

# Solution analytique
t_exact = np.linspace(t0, tf, 1000)
y_exact = solution_analytique(t_exact)

# Visualisation des résultats
plt.figure(figsize=(10, 6))
plt.plot(t_exact, y_exact, 'k-', label='Solution analytique')
plt.plot(t_euler_exp, y_euler_exp, 'b-o', label='Euler explicite', markersize=4)
plt.plot(t_euler_imp, y_euler_imp, 'g-s', label='Euler implicite', markersize=4)
plt.plot(t_rk4, y_rk4, 'r-^', label='Runge-Kutta 4', markersize=4)
plt.xlabel('Temps t')
plt.ylabel('Solution y(t)')
plt.title('Comparaison des méthodes de résolution numérique')
plt.legend()
plt.grid()
plt.show()


