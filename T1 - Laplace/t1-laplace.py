import sys
import control as ctl
import matplotlib.pyplot as plot
import numpy as np

from utils import *

saida = []
entrada = []

Gera_Polinomio(saida, entrada)
print(saida, entrada)
# A função tf do módulo control faz uma função de transferência com os argumentos de saída e entrada
H = ctl.tf(saida, entrada)
print('H(s)=', H)

# módulo control faz o cálculo de polos e zeros da função de transferência
polos=ctl.pole(H) 
zeros=ctl.zero(H)

# Mostra os polos e zeros no terminal
print('Polos =', polos)
print('Zeros =', zeros)

# Gera um diagrama dos polos e zeros
diagrama_pz = plot.figure() 
ctl.pzmap(H, 1, 0, 'Diagrama de Polos e Zeros de H(s)')
plot.show() # Gera o diagrama de polos e zeros da função de transferência

# Tempo para cálculo da resposta ao impulso
T = 50 # 50 segundos
T = np.linspace(-1., T, 1000)

# O try except serve para caso o numerador seja maior que o denominador
try:
    T_saida, Y_saida = ctl.impulse_response(H, T[T>0]) ##calcula a resposta ao impulso
except:
    sys.exit("Erro na resposta ao impulso. Encerrando o programa.") # Caso dê erro, encerra o programa

# Plot dos resultados obtidos
resp_impulso = plot.figure()
plot.plot(T_saida, Y_saida, 'k-')
plot.xlabel('Tempo(s)')
plot.ylabel('Saída')
plot.legend(['Resposta ao impulso'])
plot.grid()
plot.show()

fig_3d = plot.figure(figsize=(10,10))
axis = plot.axes(projection='3d')

# Define o intervalo do gráfico e o passo de cálculo
x = np.arange(-5,5,0.25)
y = np.arange(-5,5,0.25)
X, Y = np.meshgrid(x,y)

s = X + Y*1J    # Define s como número complexo
numerador = np.polyval(saida, s)        
denominador = np.polyval(entrada, s)        
Z = abs(np.divide(numerador,denominador)) # Define a magnitude dividindo numerador pelo denominador

# Faz o plot em 3d
mag = axis.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plot.cm.jet,  linewidth=0, antialiased=False)

# Definições do gráfico
fig_3d.colorbar(mag, shrink=0.5, aspect=5)

# Definição dos 3 eixos, sendo x real, y imaginário e z o da magnitude
mag = axis.set_xlabel('Real')
mag = axis.set_ylabel('Imaginário')
mag = axis.set_zlabel('Magnitude')

# Define o ponto de vista escolhido para o gráfico
mag = axis.view_init(00, -60)

plot.tight_layout()
plot.show()

# Por fim refaz o gráfico para mostrar somente a magnitude em 2D
mag_2d = plot.figure()
mag_2d = plot.plot(Y, Z) 
mag_2d = plot.ylabel("Magnitude")
mag_2d = plot.xlabel("Imaginário")
mag_2d = plot.title("CORTE DO GRÁFICO 3D NO EIXO SIGMA")

plot.show()