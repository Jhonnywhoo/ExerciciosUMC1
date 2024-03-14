# Fazer um algoritmo que receba um numero positivo e maior que zero, calcule e mostre
# 1. o numero digitado ao quadrado
# 2. a raiz quadrada do numero digitado

import math

print("Programa que calcula o quadrado e a raiz de um numero")

numero = int(input("Entre com o numero: "))
quadrado = pow(numero,2)
raiz = math.sqrt(numero)

print("O quadrado de %.f equivale a %.f e sua raiz equivale a %.2f" %(numero,quadrado,raiz))