import numpy as np
from math import pi
from scipy import integrate

# Tolerância escolhida
tolerancia = 0.0000001
# Pares de valores entre A e B
valores_ab = [(1, 0.95), (2, 0.90), (3, 0.75)]

def calcular_X(w, a):
    return 1 / (a + 1j * w)

def calcular_energia(B, a):
    return B / (2 * a)

for a, b in valores_ab:
    E = calcular_energia(b, a)
    relerr = (E - 0) / E
    limite = 100
    i = 0
    W = 0
    passo = pi * a

    E_W, _ = integrate.quad(lambda w: (abs(calcular_X(w, a)) ** 2) / (2 * pi), -np.inf, np.inf)

    print(f"Para a = {a} e b = {b}")
    print(f"Energia para a = {a}: {calcular_energia(1, a):.6f}")
    print(f"E_W: {E_W:.6f}")
    print(f"E: {E:.6f}")

    while abs(relerr) > tolerancia:
        if relerr > 0:
            W = W + passo
        elif relerr < 0:
            passo = passo / 2
            W = W - passo

        E_W, _ = integrate.quad(lambda w: (abs(calcular_X(w, a)) ** 2) / (2 * pi), -W, W)
        relerr = (E - E_W) / E

        i += 1

        if i > limite:
            break

    print(f"{i} iterações totais: W = {W:.6f}\nErro = {np.abs(relerr * 100):.6f}%\nEnergia = {E_W:.6f}, sendo {E_W * 2 * a:.6f}% da energia do sinal\n")
input()