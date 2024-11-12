valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
parcelas = 12 * int(input('Digite o valor em anos que você vai pagar: '))
prestacao_mensal = valor_casa / parcelas

if prestacao_mensal > (0.3 * salario):
    print('Empréstimo NEGADO!')
else:
    print('Émpréstimo CONCEDIDO!')