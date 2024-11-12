tipo_carro = str(input('Digite o tipo do carro alugado(popular/luxo): ').lower())
dias_aluguel = int(input('Digite quantos dias de alugel: '))
km_percorrido = float(input('Digite a qntd. de KMs percorridos: '))

if tipo_carro == 'popular':
    if km_percorrido <= 100:
        preco = (90 * dias_aluguel) + (0.20 * km_percorrido)
        print(f'Preço aluguel = R${preco:.2f}')
    else:
        preco = (90 * dias_aluguel) + (0.10 * km_percorrido)
        print(f'Preço aluguel = R${preco:.2f}')
elif tipo_carro == 'luxo':
    if km_percorrido <= 200:
        preco = (150 * dias_aluguel) + (0.30 * km_percorrido)
        print(f'Preço aluguel = R${preco:.2f}')
    else:
        preco = (150 * dias_aluguel) + (0.25 * km_percorrido)
        print(f'Preço aluguel = R${preco:.2f}')
else:
    print('[ERRO] Entrada inválida!')
print('Volte sempre!')
