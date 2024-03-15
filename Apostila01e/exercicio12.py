# Faça um algoritmo (Fluxograma) que leia as 3 notas de um aluno e calcule a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é: 2, 3 e 5, respectivamente.

print ("Calculo de media final com 3 notas")

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))

media = (nota1*2 + nota2*3 + nota3*5)/10

print("Sua media equivale a %.2f" %(media))