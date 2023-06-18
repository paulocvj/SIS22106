import numpy as np
import matplotlib.pyplot as plt

def MS7P1(x):
    y = np.ones_like(x)
    i = np.where(x != 0)[0]
    y[i] = np.sin(x[i]) / x[i]
    return y

omega = np.linspace(-5, 5, 200)
X = lambda omega: 2 * ((3/2) * MS7P1(omega * 3/2))**2

plt.plot(omega, X(omega), 'k-', label='X(Omega)')

plt.grid(True)
plt.axis('tight')
plt.xlabel('Omega')
plt.ylabel('X(Omega)')
plt.legend()
plt.show()
