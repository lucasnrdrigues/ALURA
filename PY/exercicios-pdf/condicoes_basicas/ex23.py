nome = str(input('Digite o seu nome: '))
sexo = str(input('Digite o seu sexo (M/F): '))
valor_compras = float(input('Digite o valor das suas compras: '))

if sexo.upper() == 'M':
    valor_compras = valor_compras - (0.05 * valor_compras)
elif sexo.upper() == 'F':
    valor_compras = valor_compras - (0.13 * valor_compras)
else:
    print('Sexo inválido!!!')

print(f'Valor total da compra: {valor_compras:.2f}')