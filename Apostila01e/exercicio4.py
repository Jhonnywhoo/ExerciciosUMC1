#Criar um algoritmo (Fluxograma) que leia o saldo de uma aplicação e imprimir o novo saldo, considerando um reajuste de 15%

print('Programa que calcula reajuste de 15% em uma aplicação.')
saldo= float(input("Entre com o saldo: "))
nsaldo = saldo * 1.15
print("Novo saldo é de: R$  %.2f" %(nsaldo) )