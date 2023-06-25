import numpy as np
from scipy.integrate import quad
import scipy as sci

# Casa da tolerância desejada 
tolerancia = 0.00001

# Dicionário com valores de Alfa e Beta para análise
valores_alfa_beta = {
      1: 0.95,
      2: 0.9,
      3: 0.75
}

def MS7P1(x):
    y = np.ones(np.shape(x))
    i = np.where(x != 0)
    y[i] = np.sin(x[i]) / x[i]
    return y

def MS7P2(tau, beta, tol):
    W = 0
    step = 2 * np.pi / tau
    X_squared = lambda omega, tau: (tau * MS7P1(omega * tau / 2))**2
    E = beta * tau
    relerr = (E - 0) / E

    while abs(relerr) > tol:
        if relerr > 0:
            W = W + step
        elif relerr < 0:
            step = step / 2
            W = W - step

        E_W, _ = quad(X_squared, -W, W, args=(tau,))
        relerr = (E - E_W) / E

    return W, E_W

def E(beta):
	return (beta * np.pi) / 2.0

def E_W(W, alpha):
	return np.arctan(W / alpha)

def Energia_W(W, alpha, beta):
    # Energia em E
	e = E(beta)

	# Energia em W
	e_w = E_W(W, alpha)

    # Retorna o erro relativo
	return np.abs(e - e_w)

for alfa, beta in valores_alfa_beta.items():
        
	res = sci.optimize.minimize_scalar(Energia_W, args=(alfa, beta), tol = tolerancia)

	print(f"Para Alfa {alfa} e beta {beta}")
	print(f"W = {res.x:.6f} e E_W = {E_W(res.x, alfa):.6f}\n")
