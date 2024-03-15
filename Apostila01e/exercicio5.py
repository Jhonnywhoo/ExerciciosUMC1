#Criar um algoritmo (Fluxograma e Pseudocódigo) que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário

print('Programa que calcula reajuste em um salário.')
salario= float(input("Entre com o salário: "))
reajuste = float(input("Entre com o percentual de aumento: "))
reajuste_aumento = salario * reajuste/100
nsaldo = salario + reajuste_aumento
print("Novo salário é de: R$  %.2f, e o valor do aumento R$ %.2f " %(nsaldo, reajuste_aumento))