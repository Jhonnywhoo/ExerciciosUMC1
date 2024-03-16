metragem = float(input("\nInforme a área em m² a ser pintada: "))
latas = (metragem + 0.1 * metragem) / 6 / 18
latas = round(latas + 0.5)
galões = (metragem + 0.1 * metragem) / 6 / 3.6
galões = round(galões + 0.5)
opção1 = latas * 80
opção1 = round(opção1, 2)
opção2 = galões * 25
opção2 = round(opção2, 2)

print('''
Em latas de 18L, será necessário %.0f lata(s), e o valor será: R$%.2f
E em galões de 3,6L será necessário %.0f galão(ões), e o valor será: R$%.2f''' % (latas, opção1, galões, opção2) )
