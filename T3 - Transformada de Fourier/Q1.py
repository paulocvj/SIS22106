import matplotlib.pyplot as plt
import numpy as np

w0 = np.pi/2
# período se torna o dobro para se tornar periódico
T = 4 
inicio_periodo = -T/2
final_periodo = T/2

t = np.arange(inicio_periodo, final_periodo, (final_periodo - inicio_periodo)/(10000))

qtd_periodos = 10

# Algoritmo para a análise da transformada
def fourier(n_periodos):
    Dn = np.zeros(n_periodos * 2 + 1, dtype=np.complex128)
    y = np.zeros(t.shape, dtype=np.complex128)
    
    for n in range(len(Dn)):
        if n == n_periodos:
            Dn[n] = (3/4) / T  # Componente DC
        else:
            nr = n - n_periodos
            Dn[n] = X(nr * w0) / T

    for k in range(len(Dn)):
        y += Dn[k] * np.exp(1j * (k - n_periodos) * w0 * t)
    
    return y

def X(w):
    # Função calculada no papel
    return (1/4 * (np.sinc(w/(4 * np.pi)) ** 2) + 1/2 * (np.sinc(w/(2 * np.pi)))) 

def func_original(x, w0):
    # Sinal original, mas de forma periódica
    tl = 1 - abs((x + 1)%((np.pi * 2)/(w0)) - 1)
    return np.multiply(tl, 0, out = tl, where = (tl < 1/2))

plt.figure(figsize=(12, 6))
plt.title('Transformada de Fourier')
plt.plot(t, func_original(t, w0), label = 'Sinal original')
plt.plot(t, fourier(qtd_periodos), label = f'{qtd_periodos} períodos')
plt.tight_layout()
plt.legend()
plt.grid(True)

plt.show()