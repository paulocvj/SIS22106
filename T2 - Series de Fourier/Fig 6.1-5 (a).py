import numpy as np
import matplotlib.pyplot as plt

# Definição da função
def y(t):
    return (t/2)*(0 <= t)*(t <= 2) + 0*((2 < t)*(t <= 4)) + (-(t-4)/2)*((4 < t)*(t <= 6)) + 0*(t > 6)

# Parâmetros
T = 8  # Período da função

N = int(input("Entre com o número de termos da Série de Fourier: "))

# Vetor de valores de t
t = np.linspace(0, T, 1000)

# Cálculo da série de Fourier
c_0 = 0  # Termo DC
c_n = np.zeros(N + 1, dtype=np.complex128)  # Coeficientes c_n
for n in range(N + 1):
    integrand = y(t) * np.exp(-1j * 2*np.pi*n*t/T)
    c_n[n] = np.trapz(integrand, t) / T

# Aproximação da série de Fourier
y_fourier = np.zeros_like(t, dtype=np.complex128)
for n in range(N + 1):
    y_fourier += c_n[n] * np.exp(1j * 2*np.pi*n*t/T)

# Ajuste de escala
y_max = np.max(np.abs(y(t)))
y_fourier *= 2  # Multiplicação por 2 para ajustar a escala

erro = np.abs(y(t) - np.real(y_fourier))

# Cálculo do erro de aproximação médio
erro_medio = np.mean(erro)

print(f'O erro de aproximação médio é: {erro_medio:.6f}')

# Gráfico do sinal original e da aproximação da série de Fourier
plt.figure(figsize=(12, 4))
plt.plot(t, y(t), 'b', linewidth=2, label='Função Original')
plt.plot(t, np.real(y_fourier), 'r--', linewidth=1, label='Aproximação de Fourier')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Aproximação da Série de Fourier')
plt.legend()

# Gráfico da magnitude e fase da série de Fourier
plt.figure(figsize=(12, 4))
n_values = np.arange(N + 1)
magnitude = np.abs(c_n)
fase = np.angle(c_n)
plt.stem(n_values, magnitude, 'g', markerfmt='go', basefmt=' ')
plt.xlabel('n')
plt.ylabel('Magnitude')
plt.title('Magnitude da Série de Fourier')

plt.figure(figsize=(12, 4))
plt.stem(n_values, fase, 'm', markerfmt='mo', basefmt=' ')
plt.xlabel('n')
plt.ylabel('Fase')
plt.title('Fase da Série de Fourier')

plt.figure(figsize=(12, 4))
plt.plot(t, erro, 'g', linewidth=2, label='Erro de Aproximação')
plt.xlabel('t')
plt.ylabel('Erro')
plt.title('Erro de Aproximação')
plt.legend()

plt.tight_layout()
plt.show()