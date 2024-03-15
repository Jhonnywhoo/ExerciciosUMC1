# Criar um algoritmo (Fluxograma e Pseudocódigo) que calcule o consumo médio de um automóvel (medido em km/l), dado que são conhecidos a distância total percorrida e o volume de combustível consumido para percorrê-la (medido em litros).

print("Programa que calcula o consumo médio de um automóvel (medido em km/l).")

D = float(input("Qual a distância percorrida: "))
V = float(input("Quantos litros de combustível foi gasto?: "))
C = D / V

print("Foi consumido ", C, " litros por km")