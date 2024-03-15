# Fazer um algoritmo que receba o numero de horas trabalhadas e o valor do salario minimo. Calcule e mostre o salario a receber seguindo as regras abaixo
# o valor da hora trabalhada vale a metade do salario minimo
# o salario bruto equivale ao numero de horas trabalhadas multiplicado pelo valor da hora trabalhada
# o imposto equivale a 3% do salario bruto
# o salario a receber equivale ao salario bruto menos o imposto
print("Programa que calcula reajuste")

horas = int(input("Entre com o numero de horas trabalhadas: "))
minimo = float(input("Valor do salario minimo: "))
horatrab = minimo/2
salariobruto = horas*horatrab
imposto = salariobruto*0.03
salariofinal = salariobruto-imposto

print("Seu salario equivale a: ",salariofinal)