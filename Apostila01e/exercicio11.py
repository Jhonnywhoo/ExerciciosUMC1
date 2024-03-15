# Pedro comprou um saco de ração com peso em quilos. Pedro possui dois gatos para os quais fornece a quantidade de ração em gramas. Faça um algoritmo (Fluxograma) que receba o peso do saco de ração e a quantidade de ração fornecida para cada gato por dia. Calcule e mostre quanto restará de ração no saco após cinco dias.

print ("Calcular quantidade de racao daqui 5 dias")

saco = int(input(("Entre com o peso do saco de racao: ")))
gato1 = int(input("Gramas de racao para o primeiro gato por dia"))
gato2 = int(input("Gramas de racao para o segundo gato por dia"))
sacoGramas = saco*1000
consumoTotal = 5*(gato1+gato2)
saco5Dias = sacoGramas-consumoTotal

print ("Voce tera %.2f gramas ao final dos 5 dias" %(saco5Dias))