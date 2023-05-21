import sys
import os
import control as ctl
import matplotlib.pyplot as plot
import numpy as np

def Gera_Polinomio(saida, entrada):
    print("Gerador de Diagrama de Polos e Zeros\n")
    print("Função de transferência: H(s) = Out(s)/In(s)\n")
    n = int(input("Entre com o grau do polinômio do numerador: \n Ex: 50s^2 + 10s - 5 -> grau 2\nGrau ->"))
    for i in range(n+1):
        x = int(input(f"Entre com o coeficiente {i+1}: "))
        saida.append(x)

    n = int(input("Entre com o grau do polinômio do denominador: \n Ex: 50s^2 + 10s - 5 -> grau 2\nGrau ->"))
    for i in range(n+1):
        x = int(input(f"Entre com o coeficiente {i+1}: "))
        entrada.append(x)
