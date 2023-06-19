import numpy as np

# Definição da função MS7P2
def MS7P2(beta, a):
    W = np.tan(beta * np.pi / 2) * a
    return W

# Valor de referência do livro
valor_referencia = 12.706

# Dicionário com os valores de 'a' e 'beta' correspondentes
valores_a_beta = {
    1: 0.95,
    2: 0.9,
    3: 0.75
}

print(f'Valor de referência utilizado na análise: {valor_referencia} rad/s\n')
# Loop para cálculo e exibição dos resultados
for a, beta in valores_a_beta.items():
    # Cálculo da largura de banda essencial
    W = MS7P2(beta, a)

    # Cálculo do erro percentual em valor absoluto
    erro_percentual = np.abs((W - valor_referencia*beta) / valor_referencia*beta) * 100

    # Exibição dos resultados
    print(f"Valor de referência com {beta*100}% do sinal: {valor_referencia*beta:.6f}")
    print(f"Largura de banda essencial (a={a}): {W:.6f} rad/s")
    print(f"Erro percentual (a={a}): {erro_percentual:.6f}%\n")

input()