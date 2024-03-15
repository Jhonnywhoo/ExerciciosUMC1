# João recebeu seu salário e precisa pagar duas contas que estão atrasadas. Como as contas estão atrasadas, João terá que pagar multa de 2% sobre cada conta. Faça um algoritmo (Fluxograma) que calcule e mostre quanto restará do salário do João.

print ("Calculo do que restara do salario")

salario = float(input("Insira seu salario em reais: "))
conta1 = float(input("Insira o valor da primeira conta em reais: "))
conta2 = float(input("Insira o valor da segunda conta em reais: "))
juros1 = conta1*1.02
juros2 = conta2*1.02
salarioResto = salario-(juros1+juros2)

print("Restarao R$ {:.2f} do seu salario apos pagar as duas contas com juros de 2%" .format(salarioResto))
