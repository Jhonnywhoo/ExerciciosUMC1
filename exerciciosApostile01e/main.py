import os
os.system('cls')

x = 0
while x < 4:
    p1 = float(input("Entre com a primeira nota: "))
    x += 1
    if p1 > 10:
        print("A nota não pode ser maior que 10.")
        break
    p2 = float(input("Entre com a segunda nota: "))
    x += 1
    if p2 > 10:
        print("A nota não pode ser maior que 10.")
        break
    tp = float(input("Entre com a nota de trabalho: "))
    x += 1
    if tp > 10:
        print("A nota não pode ser maior que 10.")
        break
    iel = float(input("Entre com a nota de laboratório: "))
    x += 1
    if iel > 1:
        print("A nota DE LABORATÓRIO não pode ser maior que 1.")
        break
else:
    np = (p1+p2+tp)*0.3 + (iel)*0.1
    print("A nota parcial desse aluno é: {:.2f}" .format(np))
    if np < 7 : {
        print("REPROVADO")
    }
    else : {
        print("APROVADO")
    }
        
    