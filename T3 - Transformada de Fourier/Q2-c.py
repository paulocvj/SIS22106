import numpy as np
import matplotlib.pyplot as plt


def MS7P1(x):
    y = np.ones_like(x)
    i = np.where(x != 0)[0]
    y[i] = np.sin(x[i]) / x[i]
    return y

omega = np.linspace(-5, 5, 20)
X = lambda omega: 1j * 2 * ((3/2) * MS7P1(omega * 3/2))**2
Dn = X(omega)

# Configuração da figura
fig = plt.figure(figsize=(8, 10))

# Espectro de Magnitude
plt.subplot(4, 1, 2)
plt.stem(omega, np.abs(Dn), 'k')
plt.xlabel('Omega')
plt.ylabel('|Dn|')
plt.xticks(np.arange(-5, 6, 1))

# Espectro de Fase
plt.subplot(4, 1, 3)
plt.stem(omega, np.angle(Dn), 'k')
plt.xlabel('Omega')
plt.ylabel('Ângulo Dn[rad]')
plt.xticks(np.arange(-5, 6, 1))

plt.tight_layout()  # Ajusta o espaçamento entre os subplots
plt.show()
