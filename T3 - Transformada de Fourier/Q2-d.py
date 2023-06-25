import numpy as np
import matplotlib.pyplot as plt

w0 = np.pi/5
T = 10
inicio_periodo = -T/2
final_periodo = T/2

t = np.arange(inicio_periodo, final_periodo, (final_periodo - inicio_periodo)/(10000))

qtd_periodos = 100

def MS7P1(x):
    y = np.ones_like(x)
    i = np.where(x != 0)[0]
    y[i] = np.sin(x[i]) / x[i]
    return y

def X(w):
    delta_t = -1 / 4 * np.sinc(w / (np.pi * 4)) ** 2
    esq_t = 1 / 2 * (3 * np.sinc(w * 3/ (np.pi * 2)) * np.exp(-1j * w))
    dir_t = (1 / (w**2)) * (np.exp(-2j * w) + 2j * w * np.exp(-2j *w) - 1) * np.exp(-1j / 2 * w)
    return dir_t + delta_t + esq_t

def fourier(n_periodos):
    Dn = np.array(np.zeros(n_periodos * 2 + 1).astype("complex128"))
    y = np.zeros(t.shape).astype("complex128")
    
    with np.nditer(Dn, op_flags=['readwrite']) as it:
        for n, x in enumerate(it):
            if n == n_periodos:
                x[...] = 3/T # Componente DC
            else:
                nr = n - n_periodos
                x[...] = X(nr * w0)/T

    for k, c in enumerate(Dn):
        y += c * np.exp(1j * (k - n_periodos) * w0 * t)
    return y

def func_original(x, w0):
    t_original = (x + 5) % ((np.pi * 2) / w0) - 5
    t_abs = abs((t_original - 1) / 3)
    t_rect = np.where(t_abs < 1/2, 1, 0)
    t_final = abs(t_original) * t_rect
    return t_final

omega = np.linspace(-5, 5, 200)

# plt.plot(omega, X(omega), 'k-', label='X(Omega)')
plt.plot(t, np.real(fourier(qtd_periodos)), label = f'{qtd_periodos} períodos')
plt.plot(t, func_original(t, w0), label = 'Sinal original')
plt.grid(True)
plt.axis('tight')
plt.xlabel('Omega')
plt.ylabel('X(Omega)')
plt.legend()
plt.show()
