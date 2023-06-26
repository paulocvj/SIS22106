import numpy as np
import matplotlib.pyplot as plt

def X(w):
    delta_t = -1 / 4 * np.sinc(w / (np.pi * 4)) ** 2
    esq_t = 1 / 2 * (3 * np.sinc(w * 3/ (np.pi * 2)) * np.exp(-1j * w))
    dir_t = (1 / (w**2)) * (np.exp(-2j * w) + 2j * w * np.exp(-2j *w) - 1) * np.exp(-1j / 2 * w)
    return dir_t + delta_t + esq_t

omega = np.linspace(-20, 20, 80)
Dn = X(omega)

# Configuração da figura
fig = plt.figure(figsize=(8, 10))

# Espectro de Magnitude
plt.subplot(4, 1, 2)
plt.stem(omega, np.abs(Dn), 'k')
plt.xlabel('Omega')
plt.ylabel('|Dn|')


# Espectro de Fase
plt.subplot(4, 1, 3)
plt.stem(omega, np.angle(Dn), 'k')
plt.xlabel('Omega')
plt.ylabel('Ângulo Dn[rad]')


plt.tight_layout()  # Ajusta o espaçamento entre os subplots
plt.show()
