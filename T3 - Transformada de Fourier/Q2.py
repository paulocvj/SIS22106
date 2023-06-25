import numpy as np
import matplotlib.pyplot as plt

def MS7P1(x):
    y = np.ones_like(x)
    i = np.where(x != 0)[0]
    y[i] = np.sin(x[i]) / x[i]
    return y

<<<<<<< HEAD:T3 - Transformada de Fourier/Q2-c.py
def X(w):
    delta_t = -1 / 4 * np.sinc(w / (np.pi * 4)) ** 2
    esq_t = 1 / 2 * (3 * np.sinc(w * 3/ (np.pi * 2)) * np.exp(-1j * w))
    dir_t = (1 / (w**2)) * (np.exp(-2j * w) + 2j * w * np.exp(-2j *w) - 1) * np.exp(-1j / 2 * w)
    return dir_t + delta_t + esq_t

omega = np.linspace(-20, 20, 80)
=======
X = lambda omega: 2 * ((3/2) * MS7P1(omega * 3/2))

omega = np.linspace(-5, 5, 20)
t = np.linspace(-5, 5, 200)

>>>>>>> 5e0c88bbf3e8d1c86e5f68acb5eb20ae4d4945a5:T3 - Transformada de Fourier/Q2.py
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
<<<<<<< HEAD:T3 - Transformada de Fourier/Q2-c.py


=======
plt.xticks(np.arange(-5, 6, 1))
>>>>>>> 5e0c88bbf3e8d1c86e5f68acb5eb20ae4d4945a5:T3 - Transformada de Fourier/Q2.py
# Espectro de Fase
plt.subplot(4, 1, 3)
plt.stem(omega, angulo_Dn, 'k')
plt.xlabel('Omega')
plt.ylabel('Ângulo Dn[rad]')
<<<<<<< HEAD:T3 - Transformada de Fourier/Q2-c.py


=======
plt.xticks(np.arange(-5, 6, 1))
>>>>>>> 5e0c88bbf3e8d1c86e5f68acb5eb20ae4d4945a5:T3 - Transformada de Fourier/Q2.py
plt.tight_layout()  # Ajusta o espaçamento entre os subplots
plt.show()
