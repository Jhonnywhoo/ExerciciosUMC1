# Dados o tamanho de um arquivo (em bits), bem como a velocidade da conexão (em bits por segundo), informe o tempo necessário para o download do arquivo(Pseudocódigo)
print('Programa que calcula o tempo necessario para download de um arquivo')
a=float(input("digite o tamanho do arquivo em bits: "))
v= float(input("Digite a velocidade de conexao bits/segundos: "))
d= a / v
print("Tempo de download é de: %.2f segundos" %(d)) 