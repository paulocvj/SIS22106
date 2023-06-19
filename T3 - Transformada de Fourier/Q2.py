import numpy as np
import matplotlib.pyplot as plt

def MS7P1(x):
    y = np.ones_like(x)
    i = np.where(x != 0)[0]
    y[i] = np.sin(x[i]) / x[i]
    return y

X = lambda omega: 2 * ((3/2) * MS7P1(omega * 3/2))

omega = np.linspace(-5, 5, 20)
t = np.linspace(-5, 5, 200)

Dn = X(omega)
val_absoluto = np.abs(Dn)
angulo_Dn = np.angle(Dn)


# Configuração da figura
fig = plt.figure(figsize=(8, 10))
# Transformada de Fourier
plt.subplot(4, 1, 1)
plt.plot(t, X(t), 'k-', label='X(Omega)')
plt.grid(True)
plt.axis('tight')
plt.xlabel('Omega')
plt.ylabel('X(Omega)')
plt.legend()
# Espectro de Magnitude
plt.subplot(4, 1, 2)
plt.stem(omega, val_absoluto, 'k')
plt.xlabel('Omega')
plt.ylabel('|Dn|')
plt.xticks(np.arange(-5, 6, 1))
# Espectro de Fase
plt.subplot(4, 1, 3)
plt.stem(omega, angulo_Dn, 'k')
plt.xlabel('Omega')
plt.ylabel('Ângulo Dn[rad]')
plt.xticks(np.arange(-5, 6, 1))
plt.tight_layout()  # Ajusta o espaçamento entre os subplots
plt.show()
