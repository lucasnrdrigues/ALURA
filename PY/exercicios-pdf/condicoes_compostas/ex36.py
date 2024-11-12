horas_ativ_mes = int(input('Digite a qntd. de horas de ativ. no mês: '))
if horas_ativ_mes < 10:
    pontos = horas_ativ_mes * 2
elif horas_ativ_mes >= 10 and horas_ativ_mes < 20:
    pontos = horas_ativ_mes * 5
else:
    pontos = horas_ativ_mes * 10

dinheiro = pontos * 0.05
print(f'Dinheiro recebido: {dinheiro:.2f}')