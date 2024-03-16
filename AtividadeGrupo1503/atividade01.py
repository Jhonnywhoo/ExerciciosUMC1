import os
os.system('cls')

print("BEM VINDO! Este programa calcula descontos de IR, INSS e Sindicato!")
salario = float(input("Insira seu salário atual em reais: "))
IR = salario*0.11
INSS = salario*0.08
sindicato = salario*0.05
salarioLiquido = salario-IR-INSS-sindicato

os.system('cls')
print("Calculando de seu salário atual de R$ {:.2f} você pagou: \n R$ {:.2f} de Imposto de Renda; \n R$ {:.2f} de INSS; \n R$ {:.2f} ao Sindicato; \n Seu alário líquido totaliza R$ {:.2f}. \n Obrigado por utilizar!" .format(salario, IR, INSS, sindicato, salarioLiquido))
