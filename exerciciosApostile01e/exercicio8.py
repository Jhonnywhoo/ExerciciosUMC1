# Criar um algoritmo (Fluxograma) que dados dois lados de um triângulo retângulo calcule e exiba a respectiva hipotenusa

import math

c1=int(input("Entre com o cateto oposto: "))
c2=int(input("Entre com o cateto adjacente: "))
hip = math.sqrt(pow(c1,2)+c2**2)
print("Hipotenusa = {:f}".format(hip))