# Sabe-se que para iluminar de maneira correta os cômodos de uma casa, para cada metro quadrado, deve-se usar 18W de potência. Faça um algoritmo (Fluxograma) que receba as duas dimensões de um cômodo (em metros). Calcule e mostre a sua área (em m2) e a potência de iluminação que deverá ser utilizada.

print("Potencia necessaria em W para os metros quadrados do comodo")
X = float(input("Insira a largura do comodo em metros: "))
Y = float(input("Insira o comprimento do comodo em metros: "))
m2 = X*Y 
necessario = round(m2*18)
print ("Serao necessarios {:.0f}W de potencia para esse comodo de {:.0f} metros quadrados." .format(necessario,m2))

