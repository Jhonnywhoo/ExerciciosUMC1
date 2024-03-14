# Faça um algoritmo (Fluxograma) que receba o peso de uma pessoa em quilos. Calcule e mostre: 
# 1. O novo peso se a pessoa engordar 15% sobre o peso digitado;
# 2. O novo peso se a pessoa emagrecer 20% sobre o peso digitado;

print("Peso se engordar 15% ou se emagrecer 20%")

peso = float(input("Insira seu peso atual em kg: "))
engordar = peso+(peso*0.15)
emagrecer = peso-(peso*0.20)
print("Se voce ganhar 15% do seu peso voce tera {:.2f} kg e se voce perder 20% do seu peso voce tera {:.2f} kg" .format(engordar,emagrecer))