# Faça um algoritmo (Fluxograma) que receba o custo de um espetáculo teatral e o preço do convite deste espetáculo. Esse algoritmo deve calcular e mostrar a quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado.

print ("Calculo de ingressos para pagar o custo")

ingresso = float(input("Valor do ingresso: "))
custo = float(input("Custo do espetaculo: "))
necessario = round((custo/ingresso)+0.5)
print("Necessario vender %.f ingressos para pagar o custo" %(necessario))
