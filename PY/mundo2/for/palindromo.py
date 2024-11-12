frase = str(input('Digite uma frase: ')).strip().upper()
junto = ''.join(frase)
inverter = ''
for letra in range(len(junto) - 1, -1, -1):
    inverter += junto[letra] # Pega a var junto e passa cada letra dela para a var inverter
print(f'Inverso: {inverter}')
if inverter == junto:
    print('É um palíndromo !')
else:
    print('Não é um palíndromo !')

print('-' * 20)
#também temos esse outro método:
junto2 = ''.join(frase)
inverter2 = junto[::-1] # pega de trás para frente

print(f'Inverso: {inverter}')
if inverter == junto:
    print('É um palíndromo !')
else:
    print('Não é um palíndromo !')
