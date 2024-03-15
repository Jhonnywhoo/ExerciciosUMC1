# Criar um algoritmo (Fluxograma) que converta segundos em minutos e segundos. Por exemplo, 252 segundos equivalem a 4 minutos e 12 segundos.

tempo = int(input("Entre com o tempo em segundos: "))
minutos = tempo//60
segundos = tempo%      60

print("O tempo em minutos e segundos é: ", minutos, ":", segundos)