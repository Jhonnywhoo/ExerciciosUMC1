# Criar um algoritmo (Fluxograma) que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre: - A idade desta pessoa hoje; - A idade desta pessoa em 2025. 

nascimento=int(input("Entre com o ano de nascimento: "))
Ano_atual=int(input("Entr com o ano atual: "))
idadeh= Ano_atual - nascimento
idadef= 2030 - nascimento
print("A pessoa tem", idadeh,"anos")
print("A pessoa terá em 2030", idadef,"anos")
